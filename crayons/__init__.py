"""crayons
v0.3.4

This is a module for special effects in the terminal.

It can change font color, background color, cursor position, and more."""

import os
import sys
import shutil
import random

ALL_COLORS = ('red', 'green', 'yellow', 'blue', 'purple', 'cyan')

def _hex_to_rgb(hx):
    hx = hx [1:]
    rgb = []
    for i in (0, 2, 4):
        rgb.append(int(hx[i:i+2], 16))
    return tuple(rgb)

def fg(color):
    """Set the foreground color for text to be printed in"""
    if color == 'random':
        color = random.choice(ALL_COLORS)

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
    """Set the background color for text to be printed in"""
    if color == 'random':
        color = random.choice(ALL_COLORS)

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
    """Set the foreground color to an RGB value"""
    print(f'\033[38;2;{r};{g};{b}m', end='')

def fg_hex(hx):
    """Set the output foreground color to a hex code"""
    print('\033[38;2;{};{};{}m'.format(*_hex_to_rgb(hx)), end='')

def bg_hex(hx):
    """Set output background to a hex code"""
    print('\033[48;2;{};{};{}m'.format(*_hex_to_rgb(hx)), end='')

def bg_rgb(r, g, b):
    """Set the background color to an RGB value"""
    print(f'\033[48;2;{r};{g};{b}m', end='')

def effect(ef):
    """Add a text effect, like bold or underline"""
    ef = {
        'bold': '\033[1m',
    }[ef]
    print(ef)

def goto(x, y):
    """Set the cursor position to a point in the terminal"""
    print(f'\033[{x};{y};H', end='')

def size():
    """Return the size of the terminal in rows and columns"""
    return (shutil.get_terminal_size()[1], shutil.get_terminal_size()[0])

def clear():
    """Rmove all printed content from the terminal"""
    os.system('clear')

def terminalbg(color):
    if sys.platform == 'linux':
        os.system(f'setterm --background {color}')
    elif sys.platform == 'win32':
        os.system(f'color {color}')
    else:
        print('''This has not yet been implemented on your platform. 
If you would like to implement it, go to 
https://github.com/Kaamkiya/crayons
and send a PR''')

def reset():
    """Reset all effects"""
    print('\033[0m', end='')
