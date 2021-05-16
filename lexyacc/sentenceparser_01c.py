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
  d['ADJECTIVE'] = 'their|my|your|his|her|its|big|green'.split('|')
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
  #if t.type == 'OTHER':
  # print('WordLexer does not know word',t.value)
  return t

class SentenceParser(Parser):
 tokens = WordLexer.tokens
 def error(self,t):
  print('parse error',t.type,t.value)
 
 # Grammar rules and actions
 # sentence : subject VERB object
 @_('subject verb object')
 def sentence(self,p):
  print("Sentence is valid.")
  #print(p)
  #print(list(p))
  for x in list(p):
   print(x)
 # sentence: adjective
 @_('adjective')
 def sentence(self,p):
  print("Sentence is valid.")
  #print(p)
  #print(list(p))
  for x in list(p):
   print(x)
  
 @_('VERB')
 def verb(self,p):
  return ['verb',['VERB',p.VERB]]
 
 # subject : NOUN | PRONOUN
 @_('NOUN')
 def subject(self,p):
  return ['subject',['NOUN',p.NOUN]]

 @_('PRONOUN')
 def subject(self,p):
  return ['subject',['PRONOUN',p.PRONOUN]]

 # object : NOUN | adjective NOUN
 @_('NOUN')
 def object(self,p):
  return ['object',['NOUN',p.NOUN]]
 @_('adjective NOUN')
 def object(self,p):
  return ['object',[['adjective',p.adjective],['NOUN',p.NOUN]]]

 # adjective : adjective ADJECTIVE | ADJECTIVE
 @_('adjective ADJECTIVE')
 def adjective(self,p):
  #print('check: p.adjective=',p.adjective)
  return p.adjective + ['ADJECTIVE',p.ADJECTIVE]

 @_('ADJECTIVE')
 def adjective(self,p):
  return ['ADJECTIVE',p.ADJECTIVE]
 
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
   
