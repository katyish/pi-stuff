""" displays a snowman on the UnicornHat """

import unicornhat as uh

#define the parts
snowman = [
[0, 3], [0, 4], [0, 5],
[1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
[2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
[3, 3], [3, 4], [3, 5],
[4, 2], [4, 3], [4, 4], [4, 5], [4, 6],
[5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7],
[6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7],
[7, 2], [7, 3], [7, 4], [7, 5], [7, 6],
]

scarf = [
[4, 2], [4, 3], [4, 4], [4, 5], [4, 6],
[5, 2],
[6, 2]
]

buttons = [
[5, 4], [7, 4]
]

eyes = [
[1, 3], [1, 5]
]

def show_snowman():
    """ light up all the parts """
    uh.rotation(270)
    for [x, y] in snowman:
        uh.set_pixel(x, y, 255, 255, 255)
    for [x, y] in scarf:
        uh.set_pixel(x, y, 255, 0, 0)
    for [x, y] in buttons:
        uh.set_pixel(x, y, 0, 0, 0)
    for [x, y] in eyes:
        uh.set_pixel(x, y, 0, 0, 255)
    #..and add an orange nose!
    uh.set_pixel(2, 4, 255, 180, 0)
    uh.show()

while True:
    show_snowman()
