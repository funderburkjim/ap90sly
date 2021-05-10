
Try to use David Beazly's "sly" to parse AP90 entries.


ap90lexer.py  # contains Ap90Lexer class based on sly.

python test01.py
First lexer example. Handles only aMSumat

python test02.py ../changes/ap90.txt ap90_tokens_02.txt
