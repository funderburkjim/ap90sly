#-*- coding:utf-8 -*-
"""simplify_changes.py
 
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

def change14a(line):
 reason = ''
 changes = [
  ('{%<ab>m.</ab> <ab>pl.</ab>%}' , '{%<ab>m.</ab>%} {%<ab>pl.</ab>%}'),
  ('{%<ab>m.</ab> dual%}' , '{%<ab>m.</ab>%} {%dual%}'),
  ('{%ad <ab>loc.</ab>%}' , '{%ad loc.%}'),
  ('{%<ab>Gr.</ab>%}' ,  '<ab>Gr.</ab>'),
  ('{%Śiva-linga%}', '{%Śiva-liṅga%}'),
  ]
 newline = line
 for old,new in changes:
  newline = newline.replace(old,new)
 return reason,newline

def change14b(line):
 reason = ''
 def f(m):
  x = m.group(0)
  y = m.group(1)
  if (',' not in y) and (';' not in y):
   return x
  parts = re.split('([,; ]+)',y)
  newparts = []
  for part in parts:
   if re.search(r'[,; ]',part):
    newparts.append(part)
   else:
    newpart = '{%' + part + '%}'
    newparts.append(newpart)
  z = ''.join(newparts)
  return z
 newline = re.sub(r'{%([^%]*[,;][^%]*)%}',f,line)
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

def change18(line):
 reason = ''
 if '{@' not in line:
  return reason,line
 changes = [
  ('{@--2.@}' , '{@--2@}'), # 67
  ('{@--3.@}' , '{@--3@}'), # 16
  ('{@1.@}' , '{@1@}'), # 51
  ('{@2@}' , '{@--2@}'), # 24
  ('{@--Comp@}' , '{@--Comp.@}'), # 57
  ('{@--Cmop.@}' , '{@--Comp.@}'), # 1
  ('{@Comp.@}' , '{@--Comp.@}'), # 6
  ('{@--6.@}' , '{@--6@}'), # 2
  ('{@1,@}' , '{@1@}'), # 1
  ('{@10@}' , '{@--10@}'), # 1
  ('{@6@}' , '{@--6@}'), # 3
  ('{@5@}' , '{@--5@}'), # 3
  ('{@4@}' , '{@--4@}'), # 5
  ('{@--12.@}' , '{@--12@}'), # 1
  ('{@7@}' , '{@--7@}'), # 2
  ('{@--9,@}' , '{@--9@}'), # 1
  ('{@3@}' , '{@--3@}'), # 3
  ('{@9@}' , '{@--9@}'), # 2
  ('{@--II.@}' , '-II.'), # 1
  ('{@--5.@}' , '{@--5@}'), # 2
  ('{@--7.@}' , '{@--7@}'), # 1
  ('{@--8.@}' , '{@--8@}'), # 3
  ('{@--10.@}' , '{@--10@}'), # 1
  ('{@--4.@}' , '{@--4@}'), # 1
  ('{@--9.@}' , '{@--9@}'), # 1
  ('{@--COMP.@}' , '{@--Comp.@}'), # 2
  ('{@1;@}' , '{@1@}'), # 2
  ('{@=4@}' , '{@--4@}'), # 1
  ('{@--Comp,@}' , '{@--Comp.@}'), # 1
  ('{@--21.@}' , '{@--21@}'), # 1
   ('{@--1@}' , '{@1@}'), # 127
 ]
 newline = line
 for old,new in changes:
  newline = newline.replace(old,new)
 return reason,newline

def reasons_update(reasons,reason):
 if reason not in reasons:
  reasons[reason] = 0
 reasons[reason] = reasons[reason] + 1
 
def init_changes(lines):
 changes = [] # array of Change objects
 metaline = None
 page = None
 change_fcns = [change18]
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

def write_changes(fileout,oldlines,d):
 n = 0
 for lnum in d:
  ilines = d[lnum]
  if len(ilines) == 2:
   continue
  n = n + 1
  # lines[ilines[0]] = N old
  # lines[ilines[1]] = N new  comment out
  # lines[ilines[2]] = N old  comment out
  # lines[ilines[3]] = N new  comment out 
  # ...
  # lines[ilines[-2]] = N old 
  # lines[ilines[-1]] = N new
  lines[ilines[1]] = ( lines[ilines[1]], lines[ilines[-1]] )
  for iline in ilines[2:]:
   # comment these out
   line = ';;; ' +  lines[iline]
   lines[iline] = line
 newlines = []
 for x in lines:
  if type(x) == tuple:
   newold,newnew = x
   newold1 = ';DUP ' + newold
   newlines.append(newnew)
   newlines.append(newold1)
  else:
   newlines.append(x)
 print(n,'duplicates')
 with codecs.open(fileout,"w","utf-8") as f:
  for line in newlines:
   f.write(line+'\n')
 print(len(newlines),"written to",fileout)

if __name__=="__main__":
 filein = sys.argv[1] #  file in format expected by updateByLine.py
 fileout = sys.argv[2] # similar format
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 d = {}
 for iline,line in enumerate(lines):
  m = re.search(r'([^ ]+) (old|new) (.*)$',line)
  if not m:
   continue
  lnum = m.group(1)
  if lnum not in d:
   d[lnum] = []
  d[lnum].append(iline)
 
 write_changes(fileout,lines,d)
