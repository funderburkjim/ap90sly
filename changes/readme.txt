
ap90_0.txt is commit
7eb0a4e505553cf218ab1b0ff7e66c778b7c864d
of   csl-orig/v02/ap90/ap90.txt
 cp /c/xampp/htdocs/cologne/csl-orig/v02/ap90/ap90.txt ap90_0.txt


python change_misc1_01.py ap90_0.txt changes_01_01.txt
# newline = re.sub(r'</ls>(-[0-9]+)',r'\1</ls>',line)
# newline = re.sub(r'</ls>-(-[0-9]+)',r'\1</ls>',newline)

python change_misc1_02.py ap90.txt changes_01_02.txt
 newline = re.sub(r'<>{#([a-zA-Z ]+)\)#}',r'<>{#\1#})',line)
 24

python change_misc1_02.py ap90.txt changes_01_03.txt
 newline = line.replace(' (#} <lbinfo','#} ( <lbinfo')
 28

python change_misc1_02.py ap90.txt changes_01_04.txt
 15

python change_misc1_02.py ap90.txt changes_01_04a.txt
 newline = re.sub(r'{#([a-zA-Z ]+)\)#}',r'<>{#\1#})',line)
 4

python change_misc1_02.py ap90.txt changes_01_05.txt
 newline = re.sub(r'{#--([a-zA-Z]+) \(([a-zA-Z]+)\)#}',r'{#--\1#} ({#\2#})',line)
 237
python change_misc1_02.py ap90.txt changes_01_06.txt
 newline = line.replace('(Ved).','(<ab>Ved.</ab>)')
 12

python change_misc1_02.py ap90.txt changes_01_07.txt
 newline = re.sub(r';%}',r'%};',line)

python change_misc1_02.py ap90.txt changes_01_08.txt
 newline = re.sub(r'\(([AP])[.]\)',r'(<ab>\1</ab>)',line)
 34

changes_01.txt  manual file.  from various sources
 changes_01_01.txt, 
python updateByLine.py ap90_0.txt changes_01.txt ap90_1.txt

changes_01.txt primarily dealing with parentheses and brackets.

changes_02.txt   will deal with additional issues:
 punctuation at end of italics

python change_misc1_02.py ap90.txt changes_02_01.txt
 ,%} -> %},;  and similarly for period.
 1039

python change_misc1_02.py ap90.txt changes_02_02.txt
 newline = re.sub(r'{%-<ab>(n|ind|f|m)\.</ab>%}',r'{%--<ab>\1.</ab>%}',line)
 5
python change_misc1_02.py ap90.txt changes_02_03.txt
 newline = re.sub(r'{%--Caus%}',r'{%--<ab>Caus.</ab>%}',line)
 7
python change_misc1_02.py ap90.txt changes_02_04.txt
 newline = re.sub(r'{%--Pass.%}',r'{%--<ab>Pass.</ab>%}',line) 
 28
python change_misc1_02.py ap90.txt changes_02_05.txt
 newline = re.sub(r'{%--(f|m|n|m),?%}',r'{%--<ab>\1.</ab>%}',line)
 18

python change_misc1_02.py ap90.txt changes_02_06.txt
 {%<ab>m.</ab> <ab>n.</ab>%}   -> {%<ab>m.</ab>%} {%<ab>f.</ab>%}
  and several other similar.
  105 instances

python change_misc1_02.py ap90.txt changes_02_07.txt
 newline = line.replace(r'{%ad. <ab>loc.</ab>%}','{%ad <ab>loc.</ab>%}')
 5

python change_misc1_02.py ap90.txt changes_02_08.txt
 fix Panini references at end of line
 27 cases

python change_misc1_02.py ap90.txt changes_02_08a.txt
 fix N. ls references at end of line
 12 cases (352 ending <ab>)
python change_misc1_02.py ap90.txt changes_02_09.txt
 abbreviations ' P. ' -> ' <ab>P.</ab> ',  and also for A.
 

python updateByLine.py ap90_1.txt changes_02.txt ap90.txt

