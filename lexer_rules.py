lx_rules = [
    (r'(?<=^( {4})*) {4}',              "'TAB'"),
    (r'[ \n\t]+',                       None),
    (r'\'\'\'',                         "'MCOMMENT'"),
    (r'\"\"\"',                         "'MCOMMENT'"),
    (r'#.*$',                           "'ICOMMENT'"),
    (r'\(',                             "'LP'"),      # Left Parentheses
    (r'\)',                             "'RP'"),      # Right Parentheses
    (r'\[',                             "'LSB'"),     # Left Square Brackets
    (r'\]',                             "'RSB'"),     # Right Square Brackets
    (r':',                              "'COLON'"),
    (r'|',                              "'BOR'"),
    (r'&',                              "'BAND'"),
    (r'\^',                             "'BXOR'"),
    (r'<<',                             "'LSHIFT'"),
    (r'>>',                             "'RSHIFT'"),
    (r'~',                              "'BNOT'"),
    (r'\+',                             "'ADD'"),
    (r'-',                              "'SUB'"),
    (r'\*\*',                           "'POW'"),     # Power
    (r'\*',                             "'MUL'"),     # Multiply
    (r'%',                              "'MOD'"),
    (r'//',                             "'DDIV'"),
    (r'/',                              "'DIV'"),
    (r'<=',                             "'LTE'"),     # Less Than or Equal
    (r'<',                              "'LT'"),      # Less Than
    (r'>=',                             "'GTE'"),     # Greater Than or Equal
    (r'>',                              "'GT'"),      # Greater Than
    (r'==',                             "'EQ'"),      # Equal
    (r'!=',                             "'NEQ'"),     # Not Equal
    (r'=',                              "'ASSIGN'"),
    (r'[+-]?([0-9]*[.e])?[0-9]+',        "'NUM'"),
    (r'([\"\'])(?:(?=(\\?))\2.)*?\1',   "'STR'"),
    (r'class\b',                        "'CLASS'"),
    (r'True\b',                         "'TRUE'"),
    (r'False\b',                        "'FALSE'"),
    (r'is\b',                           "'IS'"),
    (r'return\b',                       "'RETURN'"),
    (r'None\b',                         "'NONE'"),
    (r'continue\b',                     "'CONTINUE'"),
    (r'and\b',                          "'AND'"),
    (r'or\b',                           "'OR'"),
    (r'not\b',                          "'NOT'"),
    (r'if\b',                           "'IF'"),
    (r'elif\b',                         "'ELIF'"),
    (r'else\b',                         "'ELSE'"),
    (r'while\b',                        "'WHILE'"),
    (r'for\b',                          "'FOR'"),
    (r'def\b',                          "'DEF'"),
    (r'from\b',                         "'FROM'"),
    (r'with\b',                         "'WITH'"),
    (r'as\b',                           "'AS'"),
    (r'import\b',                       "'IMPORT'"),
    (r'pass\b',                         "'PASS'"),
    (r'break\b',                        "'BREAK'"),
    (r'in\b',                           "'IN'"),
    (r'raise\b',                        "'RAISE'"),
    (r',',                              "'COMMA'"),
    (r'\.',                             "'DOT'"),
    (r'[A-Za-z_][A-Za-z0-9_]*',         "'IDENTIFIER'")
]
