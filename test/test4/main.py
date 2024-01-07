class Colors:
    # Colores de texto
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

    # Estilos de texto
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
# ? Tokens creation
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'FUNCTION',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'RBRACKET',
    'LBRACKET',
    'EQUALS',
    'CALL',
    
    )

# ? Tokens simply definition 

t_PLUS    = r'\+'

t_EQUALS  = r'='
t_RPAREN = r'\)'
t_LPAREN = r'\('
t_ignore = ' \t\n'

t_RBRACKET = r'\}'
t_LBRACKET = r'\{'

# ? Tokens complex definition
def t_FUNCTION(t):
    r'fn'
    return t

def t_CALL(t):
    r'call'
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# ? Newline handling
def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

# ? Error handling
def t_error (t):
    print("Error: ", t.value[0])
    t.lexer.skip(1)
    
# ! Handling data of code

# ? Var names, Function names
names = {}
function_definitions = {}


# ? Parcer rules (Sintax)

def p_statement_expr(t):
    'statement : expression'
    print(f"Statement:Expression @Value={t[1]}")


def p_statement_assing (p):
    '''statement : IDENTIFIER EQUALS expression'''
    names[p[1]] = p[3]
    p[0] = {'variable': p[1], 'value': p[3]}

    print(f"{Colors.GREEN} Current variables: {names} {Colors.RESET}")


def p_expression_binop(p):
    '''expression : expression PLUS expression'''
    p[0] = p[1] + p[3]
    print(f"Expression 1: {p[1]} Expression 2: {p[3]}")
    

def p_function_definition (p):
    '''statement : FUNCTION IDENTIFIER LBRACKET statements RBRACKET
                | FUNCTION IDENTIFIER LBRACKET RBRACKET'''
    
    print(f"{Colors.MAGENTA} Function definition, 'P'len: {len(p)} {Colors.RESET}")
    
    if len(p) == 6:
        function_definitions[p[2]] = {'params': [], 'body': p[4]}
        p[0]=p[4]
    elif len(p) == 5:
        p[0]=None
        function_definitions[p[2]] = {'params': [], 'body': None}
    
    print(f"{Colors.CYAN} Current functions: {function_definitions} {Colors.RESET}")
    
def p_expression_identifier(p):
    'expression : IDENTIFIER'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_statement_function_call(p):
    '''statement : CALL IDENTIFIER'''
    function_name = p[2]
    if function_name in function_definitions:
        print(f"Calling function: {function_name}")
        result = execute_function(function_name)
        print(f"Result of function call: {result}")
    else:
        print(f"{Colors.RED}Error: Function '{function_name}' not defined{Colors.RESET}")

def execute_function(function_name):
    # Implement the logic to execute the function's body here
    # You need to go through the statements in the function's body and execute them
    function_body = function_definitions[function_name]['body']
    if function_body:
        for statement in function_body:
            execute_statement(statement)

def execute_statement(statement):
    # Implement the logic to execute a statement here
    # You need to handle different types of statements (assignment, expressions, etc.)
    if 'variable' in statement and 'value' in statement:
        names[statement['variable']] = statement['value']
    elif 'expression' in statement:
        # Handle other types of statements as needed
        pass


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_statement_multiple(p):
    '''statements : statements statement
                | statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


# ? Handling parcer error
def p_error (t):

    print(f" {Colors.MAGENTA} Syntax error at token: {t} {Colors.RESET}")


# ! Code for testing
import ply.lex as lex

data = '''
fn test {
    x = 20
    y = 30
    z = x + y
}

call test

'''

# ? Build lex analizer
lexer = lex.lex()

lexer.input(data)
    
# ? Tokenization and printing of result
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"{Colors.CYAN}[Token]: {Colors.RESET}{Colors.RED}{tok.type}")
    print(f"{Colors.CYAN}[Valor]: {Colors.RESET}{Colors.RED}'{tok.value}'{Colors.RESET}")
    print("-----------------------------------------------------------------------------")

# Compilar el parser
import ply.yacc as yacc
parser = yacc.yacc()

# Probar el parser con la entrada
result = parser.parse(data)
