#-*- coding:utf-8 -*-
"""ap90_04c.py  for ap90
 
 
"""
from __future__ import print_function
import sys, re,codecs
from parseheadline import parseheadline
from ap90lexer1c import Ap90Lexer
from sly import Parser

parserrfile = 'ap90_04c_err.txt'
ferr = codecs.open(parserrfile,"w","utf-8")

class Ap90Parser(Parser):
 tokens = Ap90Lexer.tokens
 #debugfile = 'ap90_03_dbg.txt'
 def __init__(self):
  self.rawtokens = []
  self.errtokens = []
 nparse_err = 0
 def error(self,t):
  #print('parse error',t)
  ferr.write('entry err: ' + entry.metaline + '\n')
  out = '%s' %t
  ferr.write(out+'\n')
  Ap90Parser.nparse_err = Ap90Parser.nparse_err +1
 
 # Grammar rules and actions
 # entry : header expr
 @_('header expr')
 def entry(self,p):
  return [p.header,p.expr]

 # header : NUMBER DEVA BROKENBAR | DEVA BROKENBAR | SUBHW BROKENBAR
 @_('NUMBER DEVA BROKENBAR')
 def header(self,p):
  return [('entry','%s %s %s' %(p.NUMBER,p.DEVA,p.BROKENBAR))]
 @_('DEVA BROKENBAR')
 def header(self,p):
  return [('entry','%s %s' %(p.DEVA,p.BROKENBAR))]
 @_('SUBHW BROKENBAR')
 def header(self,p):
  return [('entry','%s %s' %(p.SUBHW,p.BROKENBAR))]
 
 # expr : expr term | term 
 @_('expr term')
 def expr(self,p):
  # conjunction of lists
  return p.expr + p.term
 @_('term')
 def expr(self,p):
  return p.term
 
 # term : text | raw | deva | ls | parenterm | bracket
 @_('text')
 def term(self,p):
  return p.text
 @_('raw')
 def term(self,p):
  return p.raw
 @_('deva')
 def term(self,p):
  return p.deva
 @_('ls')
 def term(self,p):
  return p.ls
 @_('parenterm')
 def term(self,p):
  return p.parenterm
 @_('bracket')
 def term(self,p):
  return p.bracket
 
 # parenterm : LPAREN expr RPAREN
 @_('LPAREN expr RPAREN')
 def parenterm(self,p):
  # p.expr is a list of 2-tuples (type,val)
  #eval = ' '.join([x[1] for x in p.expr])
  #print('p.expr=',p.expr)
  y = [x[1] for x in p.expr]
  #print('y=',y)
  #eval = p.expr
  eval = ' '.join(y)
  #print('eval=',eval)
  val = '( %s )' %eval
  return [('parenterm',val)]

 # bracket : LBRACKET expr RBRACKET
 @_('LBRACKET expr RBRACKET')
 def bracket(self,p):
  # p.expr is a list of 2-tuples (type,val)
  #eval = ' '.join([x[1] for x in p.expr])
  #print('p.expr=',p.expr)
  y = [x[1] for x in p.expr]
  #print('y=',y)
  #eval = p.expr
  eval = ' '.join(y)
  #print('eval=',eval)
  val = '[ %s ]' %eval
  val = re.sub(r'  +',' ',val)
  return [('bracket',val)]

 # text : text TEXT | TEXT |text ETC
 @_('text TEXT')
 def text(self,p):
  val = '%s %s' %(p.text[0][1],p.TEXT)
  return [('text',val)]
 @_('TEXT')
 def text(self,p):
  return [('text',p.TEXT)]
 @_('text ETC')
 def text(self,p):
  val = '%s %s' %(p.text[0][1],p.ETC)
  return [('text',val)]
 

 # deva : deva DEVA | DEVA | deva PUNCT 
 @_('deva DEVA')
 def deva(self,p):
  val = '%s %s' %(p.deva[0][1],p.DEVA)
  val = re.sub(r'#} +{#',' ',val)
  return [('deva',val)]
 @_('deva PUNCT')
 def deva(self,p):
  val = '%s %s' %(p.deva[0][1],p.PUNCT)
  val = re.sub(r'#} +{#',' ',val)
  return [('deva',val)]
 @_('DEVA')
 def deva(self,p):
  return [('deva',p.DEVA)]

 # ls : ls XML_LS | XML_LS | ls PUNCT
 @_('ls XML_LS')
 def ls(self,p):
  val = '%s %s' %(p.ls[0][1],p.XML_LS)
  val = re.sub(r'#} +{#',' ',val)
  return [('ls',val)]
 @_('ls PUNCT')
 def ls(self,p):
  val = '%s %s' %(p.ls[0][1],p.PUNCT)
  val = re.sub(r'#} +{#',' ',val)
  return [('ls',val)]
 @_('XML_LS')
 def ls(self,p):
  return [('ls',p.XML_LS)]
 
 #----------------------------------------------------
 @_('BRACKETDEVA', 'PARENDEVA', 'DEVA', 'ITALIC', 'BOLD', 'NUMBER',
            'PAGE', 'QUOTE', 'ETC', 'PARA', 'MDASH', 'MDASHNUM',
            'LBRACKET', 'RBRACKET',
            'BROKENBAR', 'SUBHW',
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
  val = p[0]
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
  #  extra attributes2
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

def merge_result1(arr):
 return arr
 # a is list of 2-tuples (kind,val)
 # merge sequences
 barr = []
 inseq = []
 for a in arr:
  kind,val =  a
  if kind == 'LBRACKET':
   inseq = ['[']
  elif kind == 'RBRACKET':
   inseq.append(']')
   kind1 = 'bracket'
   val1 = ' '.join(inseq)
   val1 = re.sub(r'  +',' ',val1)
   barr.append((kind1,val1))
   inseq = []
  elif inseq != []:
   inseq.append(val)
  else:
   barr.append(a)
 return barr


def check_bold1 (items):
 # items is list of 2-types
 if len(items) == 0:
  return
 # check that '--Comp.' bold item  either
 # (a) is absent
 # (b) is present, and only as the last BOLD item
 for i,item in enumerate(items):
  kind,val = item
  if val != '{@--Comp.@}':
   continue
  if (i+1) != len(items):
   # unexpected
   items[i] = (kind+'?1',val)

def check_bold2(items):
 # Check that any bold {@1@} is followed by {@--2@}
 nitems = len(items)
 for i,item in enumerate(items):
  kind,val = item
  if val != '{@1@}':
   continue
  i1 = i+1
  if not (i1<nitems):
   # ending with @1@
   kind = 'BOLD?2A'
   items[i] = (kind,val)
   continue
  """
  item1 = items[i1]
  kind1,val1 = item1
  if val1 != '{@--2@}':
   kind = 'BOLD?2B'
   items[i] = (kind,val)
  """
    
def out_method1a_err(entry):
 outarr = []
 outarr.append('; ' +entry.metaline)
 lines = entry.datalines
 lnum1 = entry.linenum1
 flag = False
 for iline,line in enumerate(lines):
  if '{@1@}' not in line:
   continue
  # remove bold markup
  newline = re.sub(r'{@1@}','',line)
  lnum = lnum1 + iline + 1
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append(';')
 for out in outarr:
  ferr.write(out+'\n')
 Ap90Parser.nparse_err = Ap90Parser.nparse_err + 1
 
def out_method1a(entry,results):
 outarr = []
 bolds = [item for item in results if item[0] == 'BOLD']
 check_bold1(bolds)
 check_bold2(bolds)
 outarr.append(entry.metaline)
 for item in bolds:
  kind,val = item
  #if kind == 'BOLD':
  outarr.append('%s: %s' %item)
  if kind.startswith('BOLD?'):
   out_method1a_err(entry)  # change records to ferr
 outarr.append(entry.lend)
 return outarr

def flatten_result(result):
 result1 = []
 for itemlist in result:
  for item in itemlist:
   # item is [(type,val)]
   result1.append(item)
 return result1

def write(fileout,entries):
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  nerr = 0
  merr = 10000
  d = {}  # catch bold errors
  for entry in entries:
   nout = nout + 1
   result1 = flatten_result(entry.result)
   #outarr = out_method1(entry,result1,d)
   outarr = out_method1a(entry,result1)
   for out in outarr:
    f.write(out+'\n')
 print(nout,"entries to",fileout)
 #for k in d.keys():
 # if re.search(r'{@(
 # print('%s # %s' %(k,d[k]))
  
def write_dbg1(fileout,entries):
 # distinct {%X%}
 d = {}
 for entry in entries:
  for itemlist in entry.result:
   for item in itemlist:
    kind = item[0]
    val = item[1]
    for m in re.finditer(r'{%([^%]*)%}',val):
     w = m.group(1)
     if w not in d:
      d[w] = 0
     d[w] = d[w] + 1
 with codecs.open(fileout,"w","utf-8") as f:
  keys = sorted(d.keys(),key = lambda x: x.lower())
  for w in keys:
   n = d[w]
   out = '%d %s' %(n,w)
   f.write(out+'\n')
 print(len(keys),'written to',fileout)

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
 #write_dbg1(fileout,entries)
 
 write(fileout,entries)
 ferr.close()
 print(Ap90Parser.nparse_err,'Parse errors written to',parserrfile)
  
