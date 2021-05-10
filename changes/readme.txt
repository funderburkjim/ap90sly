
ap90_0.txt is commit 17946214bab3fadc90ac7189d49f680eba836491 of
   csl-orig/v02/ap90/ap90.txt

python change_misc1_01.py ap90_0.txt changes_01_01.txt
# newline = re.sub(r'</ls>(-[0-9]+)',r'\1</ls>',line)
# newline = re.sub(r'</ls>-(-[0-9]+)',r'\1</ls>',newline)

changes_01.txt
 changes_01_01.txt, 
python updateByLine.py ap90_0.txt changes_01.txt ap90.txt
