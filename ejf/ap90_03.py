#-*- coding:utf-8 -*-
"""ap90_03.py  for ap90
 
 
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline
from ap90lexer1a import Ap90Lexer
from sly import Parser

class Ap90Parser(Parser):
 tokens = Ap90Lexer.tokens
 debugfile = 'ap90_03_dbg.txt'
 def __init__(self):
  self.rawtokens = []
  self.errtokens = []
  
 def error(self,t):
  #print('parse error',t)
  #print('parse error',t.type,t.value)
  #print('parse error tokens:')
  # for some reason, errtokens does not 'keep' all the items.
  #print('check error. # errtokens=',len(self.errtokens))
  #if t != None:
  # self.errtokens.append(t)
  pass
 
 # Grammar rules and actions
 # catch all
 # expr : expr expr
 @_('expr expr')
 def expr(self,p):
  # conjunction of lists
  return p.expr0 + p.expr1 

 @_('DEVA BROKENBAR')
 def expr(self,p):
  return [('entry','%s %s' %(p.DEVA,p.BROKENBAR))]

  @_('LPAREN')
  def expr(self,p):
   print('debug:',p.LPAREN)
   return [('LPAREN',p.LPAREN)]
  
 #----------------------------------------------------
 # sequence of TEXT tokens
 # expr : text
 @_('text')
 def expr(self,p):
  # p.text = [('text',val])
  val = p.text[0][1]  # 
  return [('TEXT',val)]

 # text : text TEXT | TEXT
 @_('text TEXT')
 def text(self,p):
  #print('text1:',p.text,' AND ',p.TEXT)
  val = '%s %s' %(p.text[0][1], p.TEXT)
  return [('text',val)]

 @_('TEXT')
 def text(self,p):
  return [('text',p.TEXT)]
 #----------------------------------------------------
 # sequence of DEVA tokens
 # expr : deva
 @_('deva')
 def expr(self,p):
  # p.text = [('deva',val])
  val = p.deva[0][1]  #
  # val = {#X#} {#Y#} {#Z#}
  # return {#X Y Z#}
  val = re.sub(r'#} *{#',' ',val)
  return [('DEVA',val)]

 # deva : deva DEVA | DEVA
 @_('deva DEVA')
 def deva(self,p):
  #print('deva1:',p.deva,' AND ',p.DEVA)
  val = '%s %s' %(p.deva[0][1], p.DEVA)
  return [('deva',val)]

 @_('DEVA')
 def deva(self,p):
  return [('deva',p.DEVA)]
 
 #----------------------------------------------------
 # [ expr ]
 @_('LBRACKET expr RBRACKET')
 def expr(self,p):
  #print('check:',p.expr)
  #val = 'TODO'
  # p.expr is a list of 2-tuples.  
  # join the text parts
  a = [x[1] for x in p.expr]
  val = ' '.join(a)
  val1 = '[%s]' %val
  return [('bracketexpr',val1)]
 
 #----------------------------------------------------
 # ( expr )  #this generates error
 #@_('LPAREN deva text RPAREN')  # This parses
 @_('LPAREN expr RPAREN')  # THIS ERRORS
 def expr(self,p):
  # p.expr is a list of 2-tuples.  
  # join the text parts
  a = [x[1] for x in p.expr]
  val = ' '.join(a)
  val1 = '(%s)' %val
  return [('parenexpr',val1)]
 
 #@_('')
 #def empty(self,p):
 # pass
 
 
 #@_('DEVA DEVA')
 #def expr(self,p):
 # return [('DEVA','%s %s' %(p[0],p[1]))]
 
 @_('XML_AB TEXT')
 def expr(self,p):
  ab = p[0]
  if ab == '<ab>N.</ab>':
   return [('TEXT','%s %s' %(p[0],p[1]))]
  else:
   return [('XML_AB',p.XML_AB),('TEXT',p.TEXT)]
  
 @_('BRACKETDEVA', 'PARENDEVA', 'DEVA', 'ITALIC', 'BOLD', 'NUMBER',
            'PAGE', 'QUOTE', 'ETC', 'PARA', 'MDASH', 'MDASHNUM',
            #'LBRACKET', 'RBRACKET',
            'BROKENBAR',
            # 'LPAREN', 'RPAREN',
            # 'XML0','EMPTYXML',
            'TEXT', 'PUNCT', 
            'XML_LS', 'XML_AB', 'LBINFO',
            'PARENQ', 'EQ', 'AMP', 'SPECIAL')
 def expr(self,p):
  for key in p._namemap.keys():  # there is only one key in this usage
   break
  self.rawtokens.append((key,p[0]))
  #print('Raw token',key,p[0])
  return [(key,p[0])]
 
 # entry : entry | etoken
 #
class Entry(object):
 Ldict = {}
 def __init__(self,lines,linenum1,linenum2):
  # linenum1,2 are int
  self.metaline = lines[0]
  self.lend = lines[-1]  # the <LEND> line
  self.datalines = lines[1:-1]  # the non-meta lines
  # parse the meta line into a dictionary
  #self.meta = Hwmeta(self.metaline)
  self.metad = parseheadline(self.metaline)
  self.linenum1 = linenum1
  self.linenum2 = linenum2
  #L = self.meta.L
  L = self.metad['L']
  if L in self.Ldict:
   print("Entry init error: duplicate L",L,linenum1)
   exit(1)
  self.Ldict[L] = self
  #  extra attributes
  self.marked = False # from a filter of markup associated with verbs
  self.markcode = None
  self.markline = None

def init_entries(filein):
 # slurp lines
 with codecs.open(filein,encoding='utf-8',mode='r') as f:
  lines = [line.rstrip('\r\n') for line in f]
 recs=[]  # list of Entry objects
 inentry = False  
 idx1 = None
 idx2 = None
 for idx,line in enumerate(lines):
  if inentry:
   if line.startswith('<LEND>'):
    idx2 = idx
    entrylines = lines[idx1:idx2+1]
    linenum1 = idx1 + 1
    linenum2 = idx2 + 1
    entry = Entry(entrylines,linenum1,linenum2)
    recs.append(entry)
    # prepare for next entry
    idx1 = None
    idx2 = None
    inentry = False
   elif line.startswith('<L>'):  # error
    print('init_entries Error 1. Not expecting <L>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <LEND>
    continue
  else:
   # inentry = False. Looking for '<L>'
   if line.startswith('<L>'):
    idx1 = idx
    inentry = True
   elif line.startswith('<LEND>'): # error
    print('init_entries Error 2. Not expecting <LEND>')
    print("line # ",idx+1)
    print(line.encode('utf-8'))
    exit(1)
   else: 
    # keep looking for <L>
    continue
 # when all lines are read, we should have inentry = False
 if inentry:
  print('init_entries Error 3. Last entry not closed')
  print('Open entry starts at line',idx1+1)
  exit(1)

 print(len(lines),"lines read from",filein)
 print(len(recs),"entries found")
 return recs

def lexflag(line):
 lexpatterns = [
   '?? {%m.%}',  #masculine
   '?? {%f.%}',  #feminine
   '?? {%n.%}',  #neuter
   '?? {%a.%}',  #adjective
   '?? {%ind.%}',  # indeclineable
 ]
 for pattern in lexpatterns:
  if pattern in line:
   return True
 return False



def write(fileout,entries):
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  for entry in entries:
   nout = nout + 1
   outarr = []
   outarr.append(entry.metaline)
   try:
    result = entry.result
   except:
    entry.result = None
   if entry.result == None:
    entry.result = [('ERROR','result is None')]
    outarr.append('ERROR: result is None')
    for out in outarr:
     f.write(out+'\n')
    print('STOPPING AT ERROR:',entry.metaline)
    break
   for item in entry.result:
    ttype = item[0]
    val = item[1]
    outarr.append('%s: %s' %(ttype, val))
   # lend
   outarr.append(entry.lend)
   for out in outarr:
    f.write(out+'\n')
 print(nout,"entries to",fileout)
 
if __name__=="__main__": 
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx
 fileout = sys.argv[2] 

 entries = init_entries(filein)
 lexer = Ap90Lexer()
 parser = Ap90Parser()
 #entries = [entries[1],entries[13]]
 #entries = entries[0:10]
 #entries = entries[:1]
 maxerr = 10
 numerr = 0
 for ientry,entry in enumerate(entries):
  data = '\n'.join(entry.datalines)
  try:
   parser.rawtokens = []
   parser.errtokens = []
   result = parser.parse(lexer.tokenize(data))
   entry.result = result
   if result == None:
    numerr = numerr + 1
    print('; --------------- Error number',numerr)
    print('; '+entry.metaline)
    #print('rawtokens')
    #print('len errtokens=',len(parser.errtokens))
    for tok in parser.errtokens:
     #print('; errtok=',tok)
     iline = int(tok.lineno)
     lnum = entry.linenum1 + iline
     lines = entry.datalines
     #line = lines[iline-1]
     #out = '%s old %s' %(lnum,iline)
     print(iline,len(lines))
     #print(out)
    for tok in parser.rawtokens:
     #print(tok)
     pass
    if numerr >= maxerr:
     break

   #print(result)
   #exit(0)
  except Exception as e:
   print('error from parser',e)
   #for tok in lexer.tokenize(data):
   # print(tok.type, tok.value)
   exit(0)
 print('tokenizing finished')
 
 write(fileout,entries)

