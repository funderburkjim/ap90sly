from sly import Lexer

def text1():
 # ap90.txt
 #<L>12<pc>0002-b<k1>aMSumat<k2>aMSumat
 textraw = """
{#aMSumat#}¦ {%<ab>a.</ab>%} [{#aMSu-astyarTe matup#}] {@1@} <lbinfo n="Lu+minous"/>
<>Luminous, radiant; {#jyotizAM raviraMSumAn#}
<><ls>Bg. 10. 21.</ls> {@--2@} Pointed. {@--3@} Fibrous,
<>abounding in filaments (<ab>Ved.</ab>).
[Page0001-a+ 46]
<>{%--<ab>m.</ab>%} ({#mAn#}) {@1@} The sun;  <lbinfo n="vAlaKilyE#rivAMSumAn"/>
<>{#vAlaKilyErivAMSumAn#} <ls>R. 15. 10</ls>, <ls>Ki. 11. 6</ls>,  <lbinfo n="ls:Y. 3.+ 144"/>
<><ls>Y. 3. 144</ls>; sometimes the moon also. {@--2@}
<><ab>N.</ab> of the grandson of Sagara, son
<>of Asamañjasa and father of Dilīpa.
<>{@--3@} <ab>N.</ab> of a mountain; {#ºmatPalA#} <ab>N.</ab> of
<>a plant {#kadalI#} Musa Sapientum or <lbinfo n="Pa+radisiaca"/>
<>Paradisiaca. {#--tI#} 1 <ab>N.</ab> of a plant  <lbinfo n="sAla#parRI"/>
<>{#sAlaparRI#} (<ab>Mar.</ab> {#qavalA, sAlavaRa#}) Hedysarum
<>Gangeticum. {@--2@} <ab>N.</ab> of the river
<>Yamunā.
"""
 textlines = textraw.splitlines()
 return textraw

class Ap90Lexer(Lexer):
 # Set of token names. Required. This is a set Literal. Members are what?
 tokens = { BRACKETDEVA, PARENDEVA, DEVA, ITALIC, BOLD, NUMBER,
            PAGE,
            LBRACKET, RBRACKET, BROKENBAR, LPAREN, RPAREN,
            XML0 ,EMPTYXML,  TEXT, PUNCT, 
            XML_LS, XML_AB
            }
            
 # String containing ignored characters between tokens
 ignore = ' \t\n\r'
 # Regular expression rules for tokens
 PAGE = r'\[Page.*?\]'   # the ordering of these rules is important!
 BROKENBAR = '¦'
 BRACKETDEVA = r'\[{#[^#]*#}\]'
 PARENDEVA = r'\({#[^#]*#}\)'
 DEVA = r'{#[^#]*#}'
 ITALIC = r'{%.*?%}'
 BOLD = r'{@.*?@}'
 TEXT = r'[a-zA-Z][a-zA-Zāñī,;. -]*'
 NUMBER = r'[0-9]+[.]?'
 LBRACKET = r'\['
 RBRACKET = r'\]'
 LPAREN = r'\('
 RPAREN = r'\)'
 XML0 = r'<>'
 EMPTYXML = r'<[^>]+/>'
 XML_LS = r'<ls.*?</ls>'
 XML_AB = r'<ab.*?</ab>'
 #TEXT = r'[a-zA-Z-]+'
 PUNCT = r'[,;.]'
if __name__ == '__main__':
 data = text1()
 lexer = Ap90Lexer()
 for tok in lexer.tokenize(data):
  print('type=%r, value=%r' % (tok.type, tok.value))
