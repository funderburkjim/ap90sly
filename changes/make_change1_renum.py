#-*- coding:utf-8 -*-
"""make_change1_renum.py
 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 
class Change(object):
 def __init__(self,metaline,page,iline,old,new,reason,iline1,line1,new1):
  self.metaline = metaline
  self.page = page
  self.iline = iline
  self.old = old
  self.new = new
  self.reason = reason
  self.iline1 = iline1
  self.line1 = line1
  self.new1 = new1
  
def change1(line):
 reason = 'marked'
 if '</ls>' not in line:
  return reason,line
 newline = re.sub(r'</ls>(-[0-9]+)',r'\1</ls>',line)
 newline = re.sub(r'</ls>-(-[0-9]+)',r'\1</ls>',newline)
 return reason,newline

def change2(line):
 reason = ''
 newline = re.sub(r'<>{#([a-zA-Z ]+)\)#}',r'<>{#\1#})',line)
 return reason,newline

def change3(line):
 reason = ''
 newline = line.replace(' (#} <lbinfo','#} ( <lbinfo')
 return reason,newline

def change4(line):
 reason = ''
 newline = re.sub(r'\({#([a-zA-Z ]+)\)#}',r'({#\1#})',line)
 return reason,newline

def change4a(line):
 reason = ''
 newline = re.sub(r'{#([a-zA-Z ]+)\)#}',r'{#\1#})',line)
 return reason,newline

def change5(line):
 reason = ''
 newline = re.sub(r'{#--([a-zA-Z]+) \(([a-zA-Z]+)\)#}',r'{#--\1#} ({#\2#})',line)
 return reason,newline

def change6(line):
 reason = ''
 newline = line.replace('(Ved).','(<ab>Ved.</ab>)')
 if newline ==  line:
  newline = line.replace('(Ved)','(<ab>Ved.</ab>)')
 return reason,newline

def change7(line):
 reason = ''
 newline = re.sub(r';%}',r'%};',line)
 return reason,newline
 
def change8(line):
 reason = ''
 newline = re.sub(r'\(([AP])[.]\)',r'(<ab>\1.</ab>)',line)
 return reason,newline

def change9(line):
 reason = ''
 newline = re.sub(r'\(([AP])[.]\)',r'(<ab>\1.</ab>)',line)
 newline = line.replace(',%}','%},')
 newline = newline.replace('.%}','%}.') 
 return reason,newline

def change10(line):
 reason = ''
 newline = re.sub(r'{%-<ab>(n|ind|f|m)\.</ab>%}',r'{%--<ab>\1.</ab>%}',line)
 return reason,newline

def change11(line):
 reason = ''
 newline = re.sub(r'{%--Caus%}',r'{%--<ab>Caus.</ab>%}',line)
 return reason,newline

def change12(line):
 reason = ''
 newline = re.sub(r'{%--Pass[.]%}',r'{%--<ab>Pass.</ab>%}',line)
 return reason,newline

def change13(line):
 reason = ''
 newline = re.sub(r'{%--(f|m|n|m),?%}',r'{%--<ab>\1.</ab>%}',line)
 return reason,newline
def change13a(line):
 reason = ''
 newline = re.sub(r'{%m%}',r'{%<ab>m.</ab>%}',line)
 return reason,newline


def write_changes(fileout,oldlines,d):
 outrecs = []
 metaline = 'No meta line'
 prevmetaline = 'No prevmetaline'
 for iline,line in enumerate(oldlines):
  if line.startswith('<L>'):
   prevmetaline = metaline
   metaline = line
  lnum = iline+1
  if lnum not in d:
   continue
  newline = d[lnum]
  if newline == line:
   continue
  # write change transaction in format expected by updateByLine.py
  outarr = []
  if prevmetaline != metaline:
   outarr.append('; ' + metaline)
  outarr.append('%s old %s' %(lnum,line))
  outarr.append('%s new %s' %(lnum,newline))
  outarr.append('; ')
  outrecs.append(outarr)
  
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(outrecs),"written to",fileout)

def init_num_lines(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f if not x.startswith(';')]
 d = {}
 for line in lines:
  line = re.sub(r'^[*] ','',line)
  m = re.search(r'^([0-9]+) (.*)$',line)
  if m == None:
   print('FORMAT ERROR in file',filein)
   print(line)
   exit(1)
  lnum = int(m.group(1))
  # adjust lnum
  if lnum >= 147770: # first instance past nyAya
   lnum = lnum - 60  # lines delete for 30 nyAya maxims
  d[lnum] = m.group(2)
 return d

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filein1 = sys.argv[2] #  file with lines of form 'N x' (N = line number in xxx
 
 fileout = sys.argv[3] # possible change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 dlines = init_num_lines(filein1)
 write_changes(fileout,lines,dlines)
