from sly import Lexer
# adds ignore_newline to track line number
class Ap90Lexer(Lexer):
 # Set of token names. Required. This is a set Literal. Members are what?
 tokens = { BRACKETDEVA, PARENDEVA, DEVA, ITALIC, BOLD, NUMBER,
            PAGE, QUOTE, ETC, PARA, MDASH, MDASHNUM,
            LBRACKET, RBRACKET, BROKENBAR, LPAREN, RPAREN,
            XML0 ,EMPTYXML,  TEXT, PUNCT, 
            XML_LS, XML_AB, LBINFO,
            PARENQ, EQ, AMP, SPECIAL
            }
            
 # String containing ignored characters between tokens
 #ignore = ' \t\n\r'
 ignore = ' \t'
 # Try to set line number
 @_('\n+')
 def ignore_newline(self, t):
  self.lineno += len(t.value)

 # Regular expression rules for tokens
 PAGE = r'\[Page.*?\]'   # the ordering of these rules is important!
 BROKENBAR = '¦'
 BRACKETDEVA = r'\[{#[^#]*#}\]'
 PARENDEVA = r'\({#[^#]*#}\)'
 DEVA = r'{#[^#]*#}'
 ITALIC = r'{%.*?%}' 
 BOLD = r'{@.*?@}'
 MDASHNUM = r'--[0-9]+[.]?'
 TEXT = r'[a-zA-Z‘“ĀĪŪŚÆṚśḌṢ][a-zA-Z‘’āīūṛḍṭḌṣṅñṇṃśḥĀĪŪṚŚṢ,;. :\'?!œæüéè-]*'  
 QUOTE = r'[‘’“”]'   # maybe not needed
 PARENQ = r'\(\?\)'
 ETC = r'&c[.;]'
 EQ = r'='
 AMP = r'&'
 #NUMBER = r'[0-9]+[.]?'
 NUMBER = r'[0-9][0-9/-]*[.]?'
 LBRACKET = r'\['
 RBRACKET = r'\]'
 LPAREN = r'\('
 RPAREN = r'\)'
 ignore_XML0 = r'<>'
 MDASH = r'--'
 PARA = r'<P>'
 ignore_LBINFO = r'<lbinfo .*?/>'
 EMPTYXML = r'<[^>]+/>'
 XML_LS = r'<ls.*?</ls>'
 #TEXT = r'[a-zA-Z-]+'
 PUNCT = r'[,;.:?…\'^º-]'
 SPECIAL = r'[⁁§◡]'
 #XML_AB = r'<ab>.*?</ab>'
 @_(r'<ab>.*?</ab>')
 def XML_AB(self,t):
  ab = t.value[4:-5]
  if ab in ['N.','Ved.']:
   t.type = 'TEXT'
  return t
