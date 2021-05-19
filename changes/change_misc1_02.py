#-*- coding:utf-8 -*-
"""change_misc.py for ap90
 
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

def change14(line):
 reason = ''
 changes = [
  ('{%<ab>m.</ab> <ab>du.</ab>%}' , '{%<ab>m.</ab>%} {%<ab>du.</ab>%}'),
  ('{%<ab>m.</ab> <ab>f.</ab>%}' , '{%<ab>m.</ab>%} {%<ab>f.</ab>%}'),
  ('{%<ab>m.</ab> <ab>n.</ab>%}' , '{%<ab>m.</ab>%} {%<ab>n.</ab>%}'),
  ('{%18 <ab>m.</ab> <ab>pl.</ab>%}' , '{%18 <ab>m.</ab>%} {%<ab>pl.</ab>%}'),
  ('{%<ab>m.</ab>, <ab>f.</ab>%}' , '{%<ab>m.</ab>%}, {%<ab>f.</ab>%}'),
  ('{%<ab>m.</ab>, <ab>n.</ab>%}' , '{%<ab>m.</ab>%}, {%<ab>n.</ab>%}'),
 ]
 newline = line
 for old,new in changes:
  newline = newline.replace(old,new)
 return reason,newline

def change15(line):
 reason = ''
 newline = line.replace(r'{%ad. <ab>loc.</ab>%}','{%ad <ab>loc.</ab>%}')
 return reason,newline

def change16(line):
 reason = ''
 newline = re.sub(r' P[.] +<lbinfo n="ls:',' <lbinfo n="ls:P. ',line)
 return reason,newline

def change16a(line):
 reason = ''
 newline = re.sub(r'<ab>N[.]</ab> *$',' <lbinfo n="ls:N.+',line)
 return reason,newline

def change17(line):
 reason = ''
 newline = re.sub(r'([^.ā]) ([PA][.]) ',r'\1 <ab>\2</ab> ',line)
 return reason,newline

def reasons_update(reasons,reason):
 if reason not in reasons:
  reasons[reason] = 0
 reasons[reason] = reasons[reason] + 1
 
def init_changes(lines):
 changes = [] # array of Change objects
 metaline = None
 page = None
 change_fcns = [change16a]
 line1_fcns = [change16a]
 reasons = {} # counts
 for iline,line in enumerate(lines):
  line = line.rstrip('\r\n')
  if line.startswith('<L>'):
   metaline = line
   continue
  if line == '<LEND>':
   metaline = None
   continue
  if line.startswith('[Page'):
   page = line
   continue
  oldline = line
  for f in change_fcns:
   reason,newline = f(oldline)
   if newline != oldline:
    if f in line1_fcns:
     iline1 = iline + 1
     line1 = lines[iline1]
     newline1 = line1
     if (f == change16a) and (line1.startswith('<>of ')):
      continue  # not of interest
    else:
     iline1 = None
     line1 = None
     newline1 = None
    change = Change(metaline,page,iline,oldline,newline,reason,iline1,line1,newline1)
    changes.append(change)
    continue
 print(len(changes),'potential changes found')
 return changes,reasons

def change_out(change,ichange):
 outarr = []
 case = ichange + 1
 #outarr.append('; TODO Case %s: (reason = %s)' % (case,change.reason))
 ident = change.metaline
 if ident == None:
  ident = change.page
 outarr.append('; ' + ident)
 lnum = change.iline + 1
 line = change.old
 new = change.new
 outarr.append('%s old %s' % (lnum,line))
 outarr.append('%s new %s' % (lnum,new))
 outarr.append(';')
 if change.iline1 != None:
  # write a second change
  lnum = change.iline1 + 1
  line = change.line1
  new = change.new1
  outarr.append('%s old %s' % (lnum,line))
  outarr.append('%s new %s' % (lnum,new))
  outarr.append(';')
 return outarr

def write_changes(fileout,changes):
 with codecs.open(fileout,"w","utf-8") as f:
  for ichange,change in enumerate(changes):
   outarr = change_out(change,ichange)
   for out in outarr:
    f.write(out+'\n')
 print(len(changes),"written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # possible change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 changes,reasons = init_changes(lines)
 write_changes(fileout,changes)
 for reason in reasons:
  n = reasons[reason]
  print('%5d %s' %(n,reason))
