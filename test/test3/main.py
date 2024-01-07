
# ? Tokens creation
tokens = (
    'IDENTIFIER',
    'NUMBER',
    
    'PLUS',
    
    'LPAREN','RPAREN',
    'LBRACKET','RBRACKET',
    
    'EQUALS',
    
    'FUNCTION',
    )

# ? Tokens simply definition 
t_LBRACKET=r'\{'
t_RBRACKET=r'\}'

t_PLUS    = r'\+'

t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_ignore = ' \t\n'


def t_FUNCTION (t):
    r'fn'
    return t

# ? Tokens complex definition
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

def t_NUMBER (t):
    r'\d+'
    t.value = int(t.value)
    return t

# ? Newline handling
def t_newline (t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# ? Error handling
def t_error (t):
    print("Error: ", t.value[0])
    t.lexer.skip(1)
    
# ! Handling data of code

# ? Var names, Function names
names = {}

# ? Parcer rules (Sintax)

def p_program(p):
    '''program : statement
            | expression
            | function_def'''

def p_expression_number(p):
    'expression : NUMBER'

def p_expression_identifier(p):
    'expression : IDENTIFIER'

def p_expression_binop(t):
    '''expression : expression PLUS expression'''

def p_function_def (p):
    '''function_def : FUNCTION IDENTIFIER LBRACKET expression RBRACKET'''
    
    
def p_statement_assing (p):
    '''statement : IDENTIFIER EQUALS expression'''
    
    
# ? Handling parcer error
def p_error (t):

    print(f"Syntax error at token: {t}")


# ! Code for testing
import ply.lex as lex

data = '''fn sexo { }'''

# ? Build lex analizer
lexer = lex.lex()

lexer.input(data)
    
# ? Tokenization and printing of result
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


# Compilar el parser
import ply.yacc as yacc
parser = yacc.yacc()

# Probar el parser con la entrada
result = parser.parse(data)
