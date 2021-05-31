#-*- coding:utf-8 -*-
"""check_verb_sections.py
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec canno t encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

def check_section_sequence(b):
 " b is a string which is one of a small list"
 known = ["I. II.","I. II. III.","I. II. III. IV.","I. II. III. IV. V."]
 return b in known
def write_marked_entries(fileout,recs):
 entries = []
 entry = []
 for rec in recs:
  a,line = rec
  if re.search('<L>',line):
   # start new entry
   entry = [line,a]
   #print(a)
   #keep = a  # initialize keep list of all {vXv}
   continue
  if re.search('<LEND>',line):
   assert entry != []
   #entry.append(rec)
   #if flag:
   # keep = True
   #if keep:
   # # save previous entry, as it was marked
   entries.append(entry)
   #if len(entries)>5:
   # break
   # start new entry
   entry = []
   #keep = False
   continue
  if entry == []:
   # skip. Not in an entry
   continue
  # in an entry. keep rec, and update keep
  #print(a)
  entry[1] = entry[1] + a
  #print(line,a)
 
 with codecs.open(fileout,"w","utf-8") as f:
  #entries = entries[0:10]
  for entry in entries:
  # print(entry)
   meta = entry[0]
   m = re.search(r'<L>(.*?)<pc>(.*?)<k1>(.*?)<',meta)
   L,pc,k1 = (m.group(1),m.group(2),m.group(3))
   a = entry[1]
   a1 = [x[2:-2] for x in a]
   b = ' '.join(a1)
   flag = check_section_sequence(b)
   out = '%s, %s, %s: %s'% (L,pc,k1,b)
   if not flag:print('PROBLEM',out)
   f.write(out+'\n')
 print(len(entries),"written to",fileout)

def mark_lines(lines):
 recs = []
 for iline,line in enumerate(lines):
  lnum = iline + 1
  a = re.findall(r'{v.*?v}',line)
  #b = [x[2:-2] for x in a]
  #flag = ','.join(b)
  rec = (a,line)
  recs.append(rec)
 return recs
if __name__=="__main__":
 filein = sys.argv[1] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[2] # possible change transactions
 n = 0
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 
 recs = mark_lines(lines)

 write_marked_entries(fileout,recs)
