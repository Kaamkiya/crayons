"""A demo of bouncing dots with color using the module"""

import time
import random

from .__init__ import size, goto, fg_rgb, clear

print('''crayons.py
v0.3.4

This is a module to make the terminal more fun and interesting.

Wait two seconds to see the demo!''')
time.sleep(2)

WIDTH, HEIGHT = size()

dots = []

for i in range(10):
    dots.append({
        'x': random.randint(1, WIDTH),
        'y': random.randint(5, HEIGHT),
        'xvel': random.choice((-1, 1)),
        'yvel': random.choice((-1, 1)),
        'color': (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
    })

while True:
    time.sleep(0.1)
    clear()
    for i, dot in enumerate(dots):
        goto(dot['x'], dot['y'])
        print('0')
        fg_rgb(*dot['color'])

        if dot['x'] > WIDTH:
            dot['xvel'] *= -1

        if dot['x'] < 1:
            dot['xvel'] *= -1

        if dot['y'] > HEIGHT:
            dot['yvel'] *= -1

        if dot['y'] < 1:
            dot['yvel'] *= -1

        dot['x'] += dot['xvel']
        dot['y'] += dot['yvel']
