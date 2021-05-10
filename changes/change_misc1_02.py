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
 newline = line.replace('{#(#}','(')
 newline = newline.replace('{#)#}',')')
 return reason,newline

def change3(line):
 reason = '{%S.%} -> Ś.'
 newline = line.replace('{%S.%}','Ś.')
 return reason,newline

def reasons_update(reasons,reason):
 if reason not in reasons:
  reasons[reason] = 0
 reasons[reason] = reasons[reason] + 1
 
def init_changes(lines):
 changes = [] # array of Change objects
 metaline = None
 page = None
 change_fcns = [change1]
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
    iline1 = None
    line1 = None
    newline1 = None
    change = Change(metaline,page,iline,oldline,newline,reason,iline1,line1,newline1)
    changes.append(change)
    continue
    m = re.search(r'<lbinfo n="ls:(.*?)[+]"/>',newline)
    pfx = m.group(1)
    # get preceding line
    iline1 = iline + 1
    line1 = lines[iline1]
    if line1.startswith('[Page'):
     iline1 = iline1 + 1
     line1 = lines[iline1]
    m1 = re.search(r'<>([0-9]+)([.] [0-9]+[.]?)',line1)
    if m1:
     a = m1.group(1)
     b = m1.group(2)
     c = a+b
     newline1 = re.sub(r'[0-9]+)([.] [0-9]+[.]?)',r'<><ls>%s \1\2</ls>'%c,line1)
     newline = re.sub(r'(<lbinfo n="ls:.*?[+])("/>)',r'\1%s\2'%a,newline)
    else:
     newline1 = re.sub(r'<>',r'<x>',line1)
    #if not m:
    # continue
    #newline1 = re.sub(r'<>([0-9]+[.] [0-9]+[.]?)',r'<><ls n=".">\1</ls>',line1)
    change = Change(metaline,page,iline,oldline,newline,reason,iline1,line1,newline1)
    changes.append(change)
    reasons_update(reasons,reason)
   oldline = newline
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
 #
 """
 lnum1 = change.iline1 + 1
 outarr.append('%s old %s' % (lnum1,change.line1))
 outarr.append('%s new %s' % (lnum1,change.new1))
 outarr.append(';')
 """
 # dummy next line
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
