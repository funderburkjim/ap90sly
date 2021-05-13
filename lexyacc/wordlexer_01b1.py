from sly import Lexer

class WordLexer(Lexer):
 tokens = {VERB,OTHER,ADVERB,PREPOSITION,CONJUNCTION,ADJECTIVE,PRONOUN}
 # String containing ignored characters between tokens
 ignore = ' \t\n\r'
 #VERB = r'\b(is|am|are|were|was|be|being|been|does|do|did|will|would|should|can|could|has|have|had|go)\b'
 #ADVERB=r'\b(very|simply|gently|quietly|calmly|angrily)\b'
 #PREPOSITION=r'\b(to|from|behind|above|below|between|below)\b'
 #CONJUNCTION=r'\b(if|then|and|but|or)\b'
 #ADJECTIVE=r'\b(their|my|your|his|her|its)\b'
 #PRONOUN=r'\b(I|you|he|she|we|they)\b'

 
 @_(r'[a-zA-Z]+')
 def OTHER(self,t):
  d = {}
  d['VERB'] = 'is|am|are|were|was|be|being|been|does|do|did|will|would|should|can|could|has|have|had|go'.split('|')
  d['ADVERB'] = 'very|simply|gently|quietly|calmly|angrily'.split('|')
  d['PREPOSITION'] = 'to|from|behind|above|below|between|below'.split('|')
  d['CONJUNCTION'] = 'if|then|and|but|or'.split('|')
  d['ADJECTIVE'] = 'their|my|your|his|her|its'.split('|')
  d['PRONOUN'] = 'I|you|he|she|we|they'.split('|')
  d['OTHER']=()
  for token in WordLexer.tokens:
   if t.value in d[token]:
    t.type = token
    break
  return t
 
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
   
