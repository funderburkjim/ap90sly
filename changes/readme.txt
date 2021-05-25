
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
 

python updateByLine.py ap90_1.txt changes_02.txt ap90_2.txt

# ap90_2.txt copied to csl-orig/v02/ap90/ap90.txt
  commit 9256711b47279c15b4200c1f20d33034422fb0b7

python change_misc1_02.py ap90.txt changes_03_01.txt
python change_misc1_02.py ap90.txt changes_03_02.txt

python change_misc1_02.py ap90_2.txt changes_03_03.txt
 regularize bold text.  390 changes

changes_03_04.txt  Bold markup for first section: {@1@}  600+
changes_03_05.txt  No bold markup AFTER {@--Comp.@}  155 cases
  Also, 5 'double' {@--Comp.@} e.g. L=3946, ayAta  Removed 2nd
changes_03_06.txt  ;{@1@} as last BOLD markup. 115 cases  {@1@} removed
changes_03_07.txt Further correct {@1@} anomalies
  a-  @1@ not followed by @2@

python make_change1.py ap90.txt ap90_04e_err.txt changes_03_08.txt

python updateByLine.py ap90_2.txt changes_03.txt ap90.txt

# handle multiple changes within changes_03, so final results easier to interpret.
python simplify_changes.py changes_03.txt changes_03_rev.txt
143 duplicates (lines changed more than once in changes_03.txt).
# check
# 1. apply changes_03_rev
python updateByLine.py ap90_2.txt changes_03_rev.txt ap90_rev.txt
# 2. confirm ap90.txt and ap90_rev.txt are the same
diff ap90.txt ap90_rev.txt | wc -l
0  # there are no differences, as desired
# ap90_rev.txt no long needed.
rm ap90_rev.txt

## We now commit ap90.txt to csl-orig/v02/ap90/ap90.txt, as commit
  f6c510d662ea06037ae49434f9a62d7a1ffcf6e2
## And prepare for further changes here by
  renaming ap90.txt as ap90_3.txt
## Next round of changes will be in changes_04.txt

changes_04.txt
# class numbers at end of lines
  Search for numbers (1-10) at end of lines, with next line <ab>[PAU].</ab>
  and move the class number to next line.
  Example:
  OLD
  xxx 1
  <><ab>P.</ab> yyy
  NEW
  xxx <lbinfo n="1+P."/>
  <>1 <ab>P.</ab> yyy
 python change_misc1_02.py ap90.txt changes_04_01.txt
 26 changes
# mark all class numbers as {cNc}  ['c' for 'class']
 python change_misc1_02.py ap90.txt changes_04_02.txt
 3589 changes
# misc. changes
# mark all section numbers starting with '--' and preceded by '>' or ' '
  --N. -> {N}   Note '--' and '.' dropped.
  Usually, but not always, -- precedes (except for 1) and period follows. 
 python change_misc1_02.py ap90.txt changes_04_03.txt
 7108 changes in 6418 lines.

# mark N. <ab>P.</ab> as {cNc} <ab>P.</ab>.  About 200

# mark sections that Don't start with '--'  I.e., a naked number in context:
 preceded by <> OR
 preceded by space BUT not in <ls>..</ls> and not in <lbinfo.../>
 python change_misc1_02.py ap90.txt changes_04_05.txt
 6895 lines changed.

python make_change1.py ap90.txt temp_lnum_entries.txt changes_04_06.txt
 misc. changes based on odd placement of numbers.  Manual.  Mostly ls corrections
 
python entries_from_lnum.py ap90.txt temp.txt temp_lnum_entries.txt

python updateByLine.py ap90_3.txt changes_04.txt ap90.txt
