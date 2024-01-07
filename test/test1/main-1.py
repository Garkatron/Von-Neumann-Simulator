from ply import lex
import ply.yacc as yacc

# Definición de tokens
tokens = (
    # ? BASIC DATA TYPES
    'NUMBER',
    'STRING',
    'NEWLINE',
    
    # ? CUSTOM DATA TYPES
    'MEMPOS',
    
    # ? ARITMETIC OPERATORS
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    
    # ? SPECIAL CHARS
    'COMMA',
    'LPAREN',
    'RPAREN',
    'COLON',
    
    'RBRACKET',
    'LBRACKET',
    
    # ? EXPRESSIONS
    'FUNCTION',
    'ID',
    
    # ? NATIVE FUNCTIONS
    'PRT'
)

# ? Regular expressions with simply declaration
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_COLON = r':'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_RBRACKET = r'\}'
t_LBRACKET = r'\{'

t_ignore_COMMENT = r'//.*' 
t_ignore = ' \t\n'



t_COMMA = r','
t_NUMBER = r'\d+(\.\d+)?'
t_STRING = r'\".*?\"'

t_MEMPOS = r'\$\d+'

#t_FUNCTION = r'FUN\b'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

# ? Regular expressions with complex declaration
def t_PRT(t):
    r'PRT'
    return t

# detect new lines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



def t_FUNCTION(t):
    r'FUN\b'
    return t


# ? Handling errors
def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)
    
# ! Code for testing
data = ''''''

# ? Build lex analizer
lexer = lex.lex()

lexer.input(data)

# ? Production gramatic rules

def p_expression_prt(t):
    'statement : PRT MEMPOS'
    print("PRT: ", t[2])
    
def p_empty(t):
    'empty :'
    print("VACIO")
    pass

def p_statements(t):
    '''statements : statements statement
                | statement
                | empty'''
                
    if len(t) == 3:
        t[0] = t[1] + [t[2]]  # Si hay más de una declaración, combina las listas
    elif len(t) == 2:
        t[0] = [t[1]]         # Si hay una única declaración, crea una lista
    else:
        t[0] = []             # Si no hay declaraciones, almacena una lista vacía
                
def p_code_block(t):
    '''code_block : LBRACKET statements RBRACKET
                | LBRACKET empty RBRACKET
                | LBRACKET RBRACKET'''
    if len(t) == 4:
        t[0] = t[2]  # Si hay declaraciones, almacena el contenido
    else:
        t[0] = []    # Si no hay declaraciones, almacena una lista vacía
        
def p_expression_func(t):
    '''statement : FUNCTION ID LBRACKET code_block RBRACKET'''
    t[0] = {'type': 'function', 'name': t[2], 'code_block': t[4]}
    print({'type': 'function', 'name': t[2], 'code_block': t[4]})

def p_error(t):
    print(f"Parser Error at token '{t.value}' at line {t.lineno}, position {t.lexpos}")

    t.lexer.skip(1)

# ! ------- ------- TESTING ------- ------- ! #



# ? Tokenization and printing of result
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

print("__________________________________________")
parser = yacc.yacc()
result = parser.parse(data)
