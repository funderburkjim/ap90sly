#-*- coding:utf-8 -*-
"""ap90_03a.py  for ap90
 
 
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline
from ap90lexer1a import Ap90Lexer
from sly import Parser

parserrfile = 'ap90_03a_err.txt'
ferr = codecs.open(parserrfile,"w","utf-8")
class Ap90Parser(Parser):
 tokens = Ap90Lexer.tokens
 #debugfile = 'ap90_03_dbg.txt'
 def __init__(self):
  self.rawtokens = []
  self.errtokens = []
  
 def error(self,t):
  #print('parse error',t)
  ferr.write('entry err: ' + entry.metaline + '\n')
  out = '%s' %t
  ferr.write(out+'\n')
 
 # Grammar rules and actions
 # entry : header expr
 @_('header expr')
 def entry(self,p):
  return [p.header,p.expr]

 # header : NUMBER DEVA BROKENBAR | DEVA BROKENBAR 
 @_('NUMBER DEVA BROKENBAR')
 def header(self,p):
  return [('entry','%s %s %s' %(p.NUMBER,p.DEVA,p.BROKENBAR))]
 @_('DEVA BROKENBAR')
 def header(self,p):
  return [('entry','%s %s' %(p.DEVA,p.BROKENBAR))]
 
 # expr : expr raw | raw 
 @_('expr raw')
 def expr(self,p):
  # conjunction of lists
  return p.expr + p.raw
 @_('raw')
 def expr(self,p):
  return p.raw
 """
 # text : text TEXT | TEXT
 @_('text TEXT')
 def text(self,p):
  val = '%s %s' %(p.text,p.TEXT)
  return [('text',val)]
 @_('TEXT')
 def text(self,p):
  return [('text',p.TEXT)]
 """
 #----------------------------------------------------
 @_('BRACKETDEVA', 'PARENDEVA', 'DEVA', 'ITALIC', 'BOLD', 'NUMBER',
            'PAGE', 'QUOTE', 'ETC', 'PARA', 'MDASH', 'MDASHNUM',
            'LBRACKET', 'RBRACKET',
            'BROKENBAR',
             'LPAREN', 'RPAREN',
            # 'XML0','EMPTYXML',
            'TEXT', 'PUNCT', 
            'XML_LS', 'XML_AB', 'LBINFO',
            'PARENQ', 'EQ', 'AMP', 'SPECIAL')
 def raw(self,p):
  for key in p._namemap.keys():  # there is only one key in this usage
   break
  #self.rawtokens.append((key,p[0]))
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
   '¦ {%m.%}',  #masculine
   '¦ {%f.%}',  #feminine
   '¦ {%n.%}',  #neuter
   '¦ {%a.%}',  #adjective
   '¦ {%ind.%}',  # indeclineable
 ]
 for pattern in lexpatterns:
  if pattern in line:
   return True
 return False

def write(fileout,entries):
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  nerr = 0
  merr = 10000
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
    #outarr.append('ERROR: result is None')
    # trap for bad first line
    outarr = [('; ' + entry.metaline)]
    """
    line = entry.datalines[0]
    lnum = entry.linenum1 + 1
    outarr.append('%s old %s' %(lnum,line))    
    # {#X#},¦ {#Y#} -> {#X, Y#}¦ 
    newline = re.sub(r'#},¦ {#(.*?)#}',  r', \1#}¦ ',line)
    if newline != line:
     outarr.append('%s new %s' %(lnum,newline))
    else:
     newline = re.sub(r'^({#[^#]*#})\^([0-9]+[.]?) *¦',r'\2 \1¦',line)
     if newline != line:
      outarr.append('%s new1 %s' %(lnum,newline))
     else:
      outarr.append('%s newX %s' %(lnum,newline))
    """
    
    for token in entry.rawtokens:
     out = 'raw: %s %s' %(token.type,token.value)
     outarr.append(out)
    for out in outarr:
     f.write(out+'\n')
    nerr = nerr + 1
    if nerr >= merr:
     print('STOPPING AT ERROR:',nerr,'in',entry.metaline)
     break
    continue
   for itemlist in entry.result:
    #print('item=',item)
    # item is a list
    for item in itemlist:
     try:
      # item is 2-tuple  : type value
      out = '%s: %s' %item
      outarr.append(out)
     except:
      outarr.append('could not print item')
      print('missing item',item)
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
 maxerr = 10000
 numerr = 0
 #entries = entries[:50]
 for ientry,entry in enumerate(entries):
  data = '\n'.join(entry.datalines)
  try:
   parser.rawtokens = []
   parser.errtokens = []
   result = parser.parse(lexer.tokenize(data))
   entry.result = result
   if result == None:
    print('; --------------- Error number',numerr)
    print('; '+entry.metaline)
    entry.rawtokens = list(lexer.tokenize(data))
    numerr = numerr + 1
    if numerr >= maxerr:
     break

   #print(result)
   #exit(0)
  except Exception as e:
   print('error from parser',e)
   #for tok in lexer.tokenize(data):
   # print(tok.type, tok.value)
   print('; --------------- Error number',numerr)
   print('; '+entry.metaline)
   entry.rawtokens = list(lexer.tokenize(data))
   numerr = numerr + 1
   if numerr >= maxerr:
    break

 print('tokenizing finished')
 
 write(fileout,entries)

