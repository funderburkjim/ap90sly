
Try to use David Beazly's "sly" to parse AP90 entries.


ap90lexer.py  # contains Ap90Lexer class based on sly.

python ap90_02.py ../changes/ap90.txt ap90_tokens_02.txt
Uses Ap90Lexer class of ap90lexer.py
This uses a 'hand parser' to join some tokens.



python ap90_03.py ../changes/ap90.txt temp_ap90_tokens_03.txt
Use Ap90Lexer class of ap90lexer1.py
Also begins use of an Ap90Parser class to 'rewrite'.


