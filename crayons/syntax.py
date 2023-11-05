from keyword import kwlist

from .__init__ import *

def highlight(code, colorscheme='atom_one_dark'):
    BOOLS = (
        'True',
        'False',
        'None'
    )
    SYMBOLS = (
        '~',
        '`',
        '!',
        '@',
        '#',
        '$',
        '%',
        '^',
        '&',
        '*',
        '(',
        ')',
        '_',
        '+',
        '-',
        '=',
        '[',
        ']',
        '{',
        '}',
        '|',
        '\\',
        '/',
        '.',
        ':',
        ';',
        '<',
        '>'
    )
    NUMBERS = (
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8' ,
        '9'
    )
    KEYWORDS = (
        '__peg_parser__',
        'and',
        'assert',
        'async',
        'await',
        'break',
        'class',
        'continue',
        'def',
        'del',
        'elif',
        'else',
        'except',
        'finally',
        'for',
        'from',
        'global',
        'if',
        'import',
        'is',
        'lambda',
        'nonlocal',
        'not',
        'or',
        'pass',
        'raise',
        'return',
        'try',
        'while',
        'with',
        'yield'
    )
    BUILTINS = tuple(dir(__builtins__))
    
    COLORS = {
        'atom_one_dark': {
            'normal': '#abb2bf',
            'keyword': '#c678dd',
            'builtin': '#56b6c2',
            'string': '#98c379',
            'number': '#d19a66'
        },
        'github': {
            'background': '#ffffff',
            'normal': '#000000',
            'keyword': '#000000',
            'builtin': '#445588',
            'string': '#dd1144',
            'number': '#009999'
        }
    }
    
    lexeme = ''
        
    for i, char in enumerate(code):
        lexeme += char
        if lexeme in KEYWORDS:
            fg_hex(COLORS[colorscheme]['keyword'])
            print(lexeme, end='')
            lexeme = ''

        if lexeme in SYMBOLS:
            fg_hex('#61afef')
            print(lexeme, end='')
            lexeme = ''

        if lexeme in BOOLS:
            fg_hex(COLORS[colorscheme]['keyword'])
            print(lexeme, end='')
            lexeme = ''

        if lexeme in NUMBERS:
            fg_hex(COLORS[colorscheme]['number'])
            print(lexeme, end='')
            lexeme = ''

        if lexeme in BUILTINS:
            fg_hex(COLORS[colorscheme]['builtin'])
            print(lexeme, end='')
            lexeme = ''

        if lexeme == '\n':
            print()
            lexeme = ''

        if lexeme == '\t':
            print(lexeme, end='')
            lexeme = ''

        if char == ' ':
            fg_hex(COLORS[colorscheme]['normal'])
            print(lexeme, end='')
            lexeme = ''


        reset()
    print(lexeme)
