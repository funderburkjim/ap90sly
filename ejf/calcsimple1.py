from sly import Lexer, Parser

class CalcLexer(Lexer):
    tokens = { NAME, NUMBER, PLUS, TIMES, MINUS, DIVIDE, ASSIGN, LPAREN, RPAREN }
    ignore = ' \t'
    # Tokens
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'
    ASSIGN = r'='
class CalcParser(Parser):
    tokens = CalcLexer.tokens
    def __init__(self):
        self.names = { }
    @_('NAME ASSIGN expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr
        print('statement1=',p.NAME,p.ASSIGN,p.expr)
    @_('NUMBER')
    def expr(self, p):
        print('NUMBER=',p.NUMBER)
        return int(p.NUMBER)

    """
    @_('expr')
    def statement(self, p):
        print('expr: statement',p.statement)
    
    @_('NUMBER')
    def expr(self, p):
        print('NUMBER=',p.NUMBER)
        return int(p.NUMBER)

    @_('NAME')
    def expr(self, p):
     print('name=',p.NAME)
    """

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))
