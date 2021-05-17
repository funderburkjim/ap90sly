
ap90_0.txt is commit
   #17946214bab3fadc90ac7189d49f680eba836491 of
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


changes_01.txt  manual file.  from various sources
 changes_01_01.txt, 
python updateByLine.py ap90_0.txt changes_01.txt ap90.txt
