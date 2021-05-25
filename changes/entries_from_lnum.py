#-*- coding:utf-8 -*-
"""entries_from_lnum.py for ap90
   read file of lnums
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 


def write_marked_entries(fileout,recs):
 entries = []
 entry = []
 keep = False
 metaline = None
 for rec in recs:
  flag,line,lnum = rec
  if line.startswith('<L>'):
   # start new entry
   entry = [rec]
   keep = flag # initialize keep
   continue
  if line == '<LEND>':
   assert entry != []
   entry.append(rec)
   if flag:
    keep = True
   if keep:
    # save previous entry, as it was marked
    entries.append(entry)
   # start new entry
   entry = []
   keep = False
   continue
  if entry == []:
   # skip. Not in an entry
   continue
  # in an entry. keep rec, and update keep
  entry.append(rec)
  if flag:
   keep = True

 with codecs.open(fileout,"w","utf-8") as f:
  for entry in entries:
   for rec in entry:
    flag,line,lnum = rec
    if flag:
     out = 'X%s %s' %(lnum,line)
    else:
     out = '%s %s' %(lnum,line)
    f.write(out+'\n')
 print(len(entries),"written to",fileout)

def init_lnums(filein):
 with codecs.open(filein,"r","utf-8") as f:
  lnums = []
  for line in f:
   line = line.rstrip('\r\n')
   line = line.strip()
   m = re.search(r'^([0-9]+)',line)
   if m:
    x = m.group(1)
    lnum = int(x)
    lnums.append(lnum)
 print(len(lnums),'line numbers from',filein)
 return lnums

def mark_lines(lines,lnums):
 lnumset = set(lnums)
 recs = []
 for iline,line in enumerate(lines):
  lnum = iline + 1
  flag = (lnum in lnumset)
  rec = (flag,line,lnum)
  recs.append(rec)
 return recs
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 filelnum = sys.argv[2]  # file with line-numbers
 fileout = sys.argv[3] # possible change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 lnums = init_lnums(filelnum)
 recs = mark_lines(lines,lnums)

 write_marked_entries(fileout,recs)
