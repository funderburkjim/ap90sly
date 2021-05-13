from sly import Lexer
from sly import Parser
class WordLexer(Lexer):
 tokens = {VERB,OTHER,ADVERB,PREPOSITION,CONJUNCTION,ADJECTIVE,PRONOUN,NOUN}
 # String containing ignored characters between tokens
 ignore = ' \t\n\r'
 def __init__(self):
  d = {}
  d['VERB'] = 'is|am|are|were|was|be|being|been|does|do|did|will|would|should|can|could|has|have|had|go'.split('|')
  d['ADVERB'] = 'very|simply|gently|quietly|calmly|angrily'.split('|')
  d['PREPOSITION'] = 'to|from|behind|above|below|between|below'.split('|')
  d['CONJUNCTION'] = 'if|then|and|but|or'.split('|')
  d['ADJECTIVE'] = 'their|my|your|his|her|its'.split('|')
  d['PRONOUN'] = 'I|you|he|she|we|they'.split('|')
  d['NOUN'] = 'dog cat horse cow'.split(' ')
  d['OTHER']=()
  self.d = d
  
 @_(r'[a-zA-Z]+')
 def OTHER(self,t):
  for token in WordLexer.tokens:
   if t.value in self.d[token]:
    t.type = token
    break
  return t

class SentenceParser(Parser):
 tokens = WordLexer.tokens
 # Grammar rules and actions
 # sentence : subject VERB object
 @_('subject VERB object')
 def sentence(self,p):
  print("Sentence is valid.",[p.subject,p.VERB,p.object])
  print(list(p))
  #print(dir(p))
  
 # subject : NOUN | PRONOUN
 @_('NOUN')
 def subject(self,p):
  return p.NOUN

 @_('PRONOUN')
 def subject(self,p):
  return p.PRONOUN

 # object : NOUN
 @_('NOUN')
 def object(self,p):
  return p.NOUN
 
if __name__ == '__main__':
 lexer = WordLexer()
 parser = SentenceParser()
 while True:
  try:
   text = input('> ')
   if text == '':break
   #tokens = list(lexer.tokenize(text))
   #for token in tokens:
   # print(token.value,'is',token.type)
   result = parser.parse(lexer.tokenize(text))
  except Exception as e:
   print('ERROR',e)
   
