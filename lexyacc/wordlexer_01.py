from sly import Lexer
class WordLexer(Lexer):
 tokens = {VERB,OTHER}
 # String containing ignored characters between tokens
 ignore = ' \t\n\r'
 VERB = r'\b(is|am|are|were|was|be|being|been|does|do|did|will|would|should|can|could|has|have|had|go)\b'
 OTHER = r'[a-zA-Z]+'
 

if __name__ == '__main__':
 lexer = WordLexer()
 while True:
  try:
   text = input('> ')
   if text == '':break
   tokens = list(lexer.tokenize(text))
   for token in tokens:
    print(token.value,'is',token.type)
  except Exception as e:
   print('ERROR',e)
   
