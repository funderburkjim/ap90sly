#-*- coding:utf-8 -*-
"""simplify_changes.py
 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

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
  try:
   lines[ilines[1]] = ( lines[ilines[1]], lines[ilines[-1]] )
  except:
   print('ERROR. lnum=%s'%lnum)
   print('illines = %s' % ilines)
   exit(1)
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
  if line.startswith(';'):
   continue
  m = re.search(r'^([^ ]+) (old|new) (.*)$',line)
  if not m:
   continue
  lnum = m.group(1)
  if lnum not in d:
   d[lnum] = []
  d[lnum].append(iline)
 
 write_changes(fileout,lines,d)
