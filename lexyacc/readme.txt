
Try to use David Beazly's "sly" to parse AP90 entries.

Test code, and code working with book 'lex&yacc, 2nd edition. '


python test01.py
First lexer example. Handles only aMSumat


python test01a.py
 First stab at a parser for ap90

python wordlexer_01.py
From lex&yacc, 2nd edition. verb/non-verb lexer  Example 1_1.
 cli program.  Exits with empty string + enter-key.
 
 Recognizes VERB and OTHER.
 Uses a regex to define known words as verb.
 
python wordlexer_01a.py
From lex&yacc, 2nd edition. Example 1_2: verb, adverb,  etc.
 cli program. Recognizes, VERB, ADVERB, ... 
 similar to wordlexer_01.py

python wordlexer_01b.py
From lex&yacc, 2nd edition. Example 1_2: verb, adverb,  etc.
 cli program. Recognizes, VERB, ADVERB, ... 
 Same functionality as wordlexer_01.
 Uses an action function for OTHER, which sets the type of token
 to VERB if the token value is in a list of verbs.

python wordlexer_01b1.py
From lex&yacc, 2nd edition. Example 1_2: verb, adverb,  etc.
 cli program. Recognizes, VERB, ADVERB, ... 
 Same functionality as wordlexer_01a.
 Uses an action function for OTHER, which sets the type of token
 to VERB if the token value is in a list of verbs, and similarly
 for other word types.


python wordlexer_01b2.py
From lex&yacc, 2nd edition. Example 1_2: verb, adverb,  etc.
 cli program. Recognizes, VERB, ADVERB, ... 
 Same functionality as wordlexer_01a.
 Uses an action function for OTHER, which sets the type of token.
 Initializes known word and word-type information in __init__ function.

python sentenceparser_01.py
Example 1-7. Simple yacc sentence parser.
SentenceParser and  WordLexer

python sentenceparser_01a.py
Includes 'object : NOUN | ADJECTIVE NOUN'
Prints unknown tokens.

python sentenceparser_01b.py
object : NOUN | adjective NOUN
adjective : adjective ADJECTIVE | ADJECTIVE

So allows one or more adjectives.
I have your big green dog

[['subject', ['PRONOUN', 'I']],
 ['verb', ['VERB', 'have']],
 ['object', [['adjective', ['ADJECTIVE', 'your', 'ADJECTIVE', 'big', 'ADJECTIVE', 'green']], ['NOUN','dog']]]]
