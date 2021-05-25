
Try to use David Beazly's "sly" to parse AP90 entries.


ap90lexer.py  # contains Ap90Lexer class based on sly.

python ap90_02.py ../changes/ap90.txt temp_ap90_parse_02.txt
Uses Ap90Lexer class of ap90lexer.py
This uses a 'hand parser' to join some tokens.

python ap90_02a.py ../changes/ap90.txt temp_ap90_parse_02a.txt
Uses Ap90Lexer1 class of ap90lexer.py
does NOT use the 'hand parser' of ap90_02.py.  This means a
simplification of the 'write' function.

python ap90_02b.py ../changes/ap90.txt temp_ap90_parse_02b.txt temp_ap90_02b_dbg.txt
Writes paren and bracket misbalancing information.

python ap90_03.py ../changes/ap90.txt temp_ap90_parse_03.txt
Use Ap90Lexer class of ap90lexer1.py
Also begins use of an Ap90Parser class to 'rewrite'.

python ap90_03a.py ../changes/ap90.txt temp_ap90_parse_03a.txt
Use Ap90Lexer class of ap90lexer1.py
Also begins use of an Ap90Parser class to 'rewrite'.


python ap90_03b.py ../changes/ap90.txt temp_ap90_parse_03b.txt
Use Ap90Lexer class of ap90lexer1a.py
Also begins use of an Ap90Parser class to 'rewrite'.

python ap90_03c.py ../changes/ap90.txt temp_ap90_parse_03c.txt
Use Ap90Lexer class of ap90lexer1b.py
Also begins use of an Ap90Parser class to 'rewrite'.

python ap90_03d.py ../changes/ap90.txt temp_ap90_parse_03d.txt

python ap90_04a.py ../changes/ap90.txt temp_ap90_parse_04a.txt
# work on entry sections.  Check initial BOLD {@1@}
# Use Ap90Lexer class of ap90lexer1c.py

python ap90_04b.py ../changes/ap90.txt temp_ap90_parse_04b.txt
# work on entry sections.  
# Use Ap90Lexer class of ap90lexer1c.py
  Check {@--Comp.@} occurs only as last bold item
   155 errors
   The subsections after Comp should not be BOLD.

python ap90_04c.py ../changes/ap90.txt temp_ap90_parse_04c.txt
 {@1@} as last BOLD markup.  Remove {@1@}.

python ap90_04d.py ../changes/ap90.txt temp_ap90_parse_04d.txt
 Check that any bold {@1@} is followed by {@--2@}, 

python ap90_04e.py ../changes/ap90.txt temp_ap90_parse_04e.txt
 Check that {@--n@} is followed by either {@--Comp.@} or by {@--m@}, where
   m == n+1


python ap90_05a.py ../changes/ap90.txt temp_ap90_parse_05a.txt

