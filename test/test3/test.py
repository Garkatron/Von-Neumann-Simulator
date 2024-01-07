
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'NAME',
    'NUMBER',
    
    'LPAREN','RPAREN',
    'LBRACKET','RBRACKET',
    
    'EQUALS',
    
    'FUNCTION',
    
    )

# Tokens
t_LBRACKET=r'\{'
t_RBRACKET=r'\}'

t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_FUNCTION(t):
    r'F'
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
import ply.lex as lex

# ! Code for testing
data = '''F testing {testvar = 2}'''

# ? Build lex analizer
lexer = lex.lex()

lexer.input(data)


# dictionary of names
names = { }

def p_expressions(t):
    '''expressions : expression
                   | expressions expression'''
    # Lógica para manejar múltiples expresiones
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = t[1] + [t[2]]

def p_statement_function(t):
    '''statement : FUNCTION NAME LBRACKET expression RBRACKET
                | FUNCTION NAME LBRACKET RBRACKET
                | FUNCTION NAME LBRACKET expressions RBRACKET'''
    if len(t) == 5:
        names[t[2]] = t[4]
    else:
        names[t[2]] = {}
        
def p_statement_assign(t):
    '''statement : NAME EQUALS expressions'''

    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])
    
def p_expression_group(t):
    'expression : LBRACKET RBRACKET'
    t[0] = {} 

def p_expression_non_empty_group(t):
    '''expression : LBRACKET expression RBRACKET
                | LBRACKET expressions RBRACKET'''
    t[0] = t[2]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)

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
