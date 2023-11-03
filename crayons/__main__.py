"""A demo of bouncing dots with color using the module"""

import random

from .__init__ import size, goto, fg_rgb

print('''crayons.py
v0.3.4

This is a module to print text with color! See the demo below:''')

WIDTH, HEIGHT = size()
HEIGHT -= 6

dots = []

for i in range(10):
    dots.append({
        'x': random.randint(1, WIDTH),
        'y': random.randint(5, HEIGHT),
        'xvel': random.randint(-2, 2),
        'yvel': random.randint(-2, 2),
        'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    })

while True:
    for i, dot in enumerate(dots):
        goto(dot['x'], dot['y'])
        fg_rgb(*dot['color'])

        if dot['x'] > WIDTH:
            dot['xvel'] *= -1

        if dot['x'] < 1:
            dot['xvel'] *= -1

        if dot['y'] > HEIGHT:
            dot['yvel'] *= -1

        if dot['y'] < 6:
            dot['yvel'] *= -1

        dot['x'] += dot['xvel']
        dot['y'] += dot['yvel']
