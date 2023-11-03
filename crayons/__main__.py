import random

from .__init__ import fg, bg, effects, fg_rgb, bg_rgb

print('''crayons.py
v0.3.4

This is a module to print text with color! See the demo below:
''')

for i in range(10):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    fg_rgb(r, g, b)
    print('R: {}, G: {}, B: {}'.format(r, g, b))
