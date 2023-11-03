def fg(color):
    color = {
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m'
    }[color]
    print(color, end='')

def bg(color):
    color = {
        'red': '\033[41m',
        'green': '\033[42m',
        'yellow': '\033[43m',
        'blue': '\033[44m',
        'purple': '\033[45m',
        'cyan': '\033[46m'
    }[color]
    print(color, end='')

def fg_rgb(r, g, b):
    print('\033[38;2;%s;%s;%sm' %(r, g, b))

def bg_rgb(r, g, b):
    print('\033[48;2;%s;%s;%sm' %(r, g, b))

def effect(effect):
    effect = {
        'bold': '\033[1m',
    }[effect]
    print(effect)
