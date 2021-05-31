
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

This copied to csl-orig/v02/ap90/ap90.txt and entered as
 commit 248b0e932f323366c6d965da5c17ccfabb8b965b
Now begin work on next version.
mv ap90.txt ap90_4.txt
touch changes_05.txt

changes_05_01:  lines with '-#}'.  combine with next line as needed.
 python change_misc1_02.py ap90.txt changes_05_01.txt
   change23, then manual review. About 280 cases.
   After this, there are only 7 instances of '-#}', and these are not
   line-spanning subheadwords.

Changes_05_02: {#-[^-]
 57 matches .  Examine these and change subheadwords to '{#--' 
 python change_misc1_02.py ap90.txt changes_05_02.txt
  change24.

changes_05_03: {#--[^#-]+-[^#-]
 284 cases, most need to change.
 Example:  '{#--kuSala, -SOMqa#}' -> '{#--kuSala, --SOMqa#}'
 python change_misc1_02.py ap90.txt changes_05_03.txt
  change25.   START HERE.
 After changes, still 54 matches  (changes_05_03a.txt) -- all 'problematic'.

changes_05_04
 lines starting with  <>{#--  which are quotations, rather than subheadwords.
 change to <>--{#.
 Thus, we are trying to reserve the pattern '{#--' to subheadwords.
 93 cases found so far 
 python change_misc1_02.py ap90.txt changes_05_04.txt
 change26 -- based on list of line-numbers

changes_05_04a:
 change '{#--X#}' to '--{#X#}' when X is not a subheadword list - i.e. a phrase
   use 2 tests:  presence of another '--' in X, or X too long (25 chars or more)
 python change_misc1_02.py ap90.txt changes_05_04a.txt
 change26a.  90 instances.

changes_05_04b:
 '{#--X#} and '=' character in X.  Change {#--X = Y#} to {#--X#} = {#Y#}
 50 cases.  Also, if X contains a single quote (avagraha), move -- outside.{##}
 python change_misc1_02.py ap90.txt changes_05_04b.txt
 change26b

changes_05_04c:
 q. at end of line  (next line v.)
 Changed a few 'q.q.v.v.'  to 'q.v.'
 python change_misc1_02.py ap90.txt changes_05_04c.txt
 change26c

changes_05_05:
 '{#= ' -> '= {#'
 python change_misc1_02.py ap90.txt changes_05_05.txt
change27
 608 cases

changes_05_05a:
 '=#}' -> '#} =
 python change_misc1_02.py ap90.txt changes_05_05a.txt
change27a
 29 cases
changes_05_05b:
 Add '-' in 19 lines. 
 Ref: https://github.com/sanskrit-lexicon/AP90/issues/18#issue-904590228
 Example: {#arjUka, pf#} -> {#arj-Uka, pf#} in entry for ajjukA
 python change_misc1_02.py ap90.txt changes_05_05b.txt

changes_05_05c:
 '{#[^#]*='   62 cases.  '=' sign in Devanagari
 example under hw akfta
 OLD: {#vAgvyavahAreRa kftA; kftA = yadapatyaM BavedasyAM tanmamaM#}
 NEW: {#vAgvyavahAreRa kftA#}; {#kftA#} = {#yadapatyaM BavedasyAM tanmamaM#}
 python entries_from_regex.py ap90.txt '{#[^#]*=' temp_deva_equal.txt
  # edit temp_deva_equal.txt and make manual change at lines starting with X
  # Then remove the X at beg. of lines, and
 python make_change1.py ap90.txt temp_deva_equal.txt changes_05_05c.txt

changes_05_05d:
 muwaH incorrectly coded as headword.  Rather, it is a compound under 'nir'
 hw spelling changes: SAMrga -> SArMga, and SAMrgin -> SArMgin

python updateByLine.py ap90_4.txt changes_05.txt ap90.txt
cp ap90.txt /c/xampp/htdocs/cologne/csl-orig/v02/ap90/ap90.txt
Pushed ap90.txt to csl-orig/v02/ap90/ap90.txt, at commit 
 e8f692dc571cd24f731617830dfb5f0661d14955

In csl-orig, corrected nyAyaH. commit d0becf092883b52897de274b7d7fe59dde9ed50a
cp /c/xampp/htdocs/cologne/csl-orig/v02/ap90/ap90.txt ap90_5.txt



changes_06_01.txt
 I. -> {vI.v} markup of Roman-numeral verb sections.
 --II. -> {vII.v}
 python entries_from_regex.py ap90.txt '--[IV]+([^a-zA-Z]|$)' temp_verb_sections.txt
  

   the '^a-zA-Z' to exclude --ISvaraH, etc.
  297 entries
  280 ' I. ' -> ' {vI.v} '
      --\([IV]+[.]\) → {v\1v}
  287 --II. -> {vII.v}
   56 --III. → {vIII.v}
   15 --IV. → {vIV.v}
    1 --V. → {vV.v}
   1 cases with '--[IV]'  (no period)
   GfR: missing I.
    Also:
     under 'pf':
     old: --<ls>V. 5</ls> <ab>P.</ab> ({#pfgoti#})
     new: {vV.v} {c5c} <ab>P.</ab> ({#pfRoti#})
     under 'vas':
     old: --<ls>V. 10</ls> <ab>U.</ab> 
     new: --{vV.v} {c10c} <ab>U.</ab>

  282 {vI.v}
  293 {vII.v}  ??
 python check_verb_sections.py temp_verb_sections.org check_verb_sections.txt
   check_verb_sections has the verbs with sections (293) and the section
   sequence.
 change to check_verb_sections.org, and modify lines manually.
   python make_change1_renum.py ap90.txt  temp_verb_sections.org changes_06_01.txt
 and insert changes_06_01 into changes_06
  Corrected Missing section I in print.  Some corrected in AP57 (but not hf)
  <L>9435<pc>0348-a<k1>fj<k2>fj 
  <L>11784<pc>0433-a<k1>kliS<k2>kliS
  <L>12652<pc>0464-c<k1>gUrd<k2>gUrd(gurd)
  <L>12790<pc>0471-c<k1>grah<k2>grah
  <L>17610<pc>0658-c<k1>paw<k2>paw
  <L>19274<pc>0718-a<k1>pf<k2>pf
  <L>24199<pc>0913-c<k1>ru<k2>ru
  <L>24234<pc>0915-a<k1>ruD<k2>ruD
  <L>31486<pc>1174-a<k1>hf<k2>hf
  <L>31508<pc>1175-a<k1>heq<k2>heq
 

python updateByLine.py ap90_5.txt changes_06.txt ap90.txt

309 matches for {#--[a-zA-Z]+ +--[a-zA-Z]+#}   ??


Yet to do
 32640 matches of {#--[a-zA-Z]+#}  These likely always to be subheadwords
    or headwords variants (such as gender variants)
  3539 matches {#--[^#]+[^a-zA-Z][^#]*#}
    Some of these are multiple sub-headwords e.g. {#--X --Y#} {#--X, --Y#}, etc.
    We want to find and recode those that are NOT multiple subheadwords.
    Sometimes there is an ending comma in subheadwords, e.g. {#--X,#}.
  

python updateByLine.py ap90_5.txt changes_06.txt ap90.txt

