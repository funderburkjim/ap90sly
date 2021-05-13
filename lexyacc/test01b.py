from ap90lexer import Ap90Lexer
from sly import Parser

class Ap90Parser(Parser):
 tokens = Ap90Lexer.tokens
 # Grammar rules and actions
 @_('term term')
 def expr(self,p):
  print('expr: ',p[0],p[1])
  return   ' DONE!'
 
 @_('DEVA')
 def term(self,p):
  # p.DEVA = {#X#}
  a = p.DEVA
  b = a[2:-2]
  c = '<s>%s</s>' %b
  return c
 
 @_('BROKENBAR')
 def term(self,p):
  print('term:',p.BROKENBAR)
  return p.BROKENBAR

def text1a():
 textraw = '''
{#aMSumat#}¦ 
'''
 return textraw

if __name__ == '__main__':
 lexer = Ap90Lexer()
 parser = Ap90Parser()
 data = text1a()
 tokengen = lexer.tokenize(data)
 tokens = list(tokengen)
 for token in tokens:
  print(token.type,token.value)
 result = parser.parse(lexer.tokenize(data))
 #result =parser.parse(tokens) # error: 'list' object is not an iterator
 #result = parser.parse(tokengen)  # gives 'sly: Parse error in input. EOF'
 print(result)
 
 #for tok in lexer.tokenize(data):
 # print('%s: %s' % (tok.type, tok.value))
