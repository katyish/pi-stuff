""" displays an xmas tree, with sort-of random fairy lights """

import unicornhat as uh
import time
import random

#define the tree parts

trunk = [[7, 2], [7, 3], [7, 4]]

tree = [[1, 3],
[2, 2], [2, 3], [2, 4],
[3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
[4, 2], [4, 3], [4, 4],
[5, 1], [5, 2], [5, 3], [5, 4], [5, 5],
[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6]]

def light_trunk():
    """ light up the tree trunk """
    for [x, y] in trunk:
        uh.set_pixel(x, y, 255, 200, 150)
        uh.show()

def light_star():
    """ light up the star """
    uh.set_pixel(0, 3, 255, 255, 0)
    uh.show()

def light_tree():
    """ light up the tree """
    for [x, y] in tree:
        uh.set_pixel(x, y, 0, 255, 0)
        uh.show()

def light_on():
    """ pick a pixel at random, turn it red, then return its position """
    light = random.choice(tree)
    #print light
    uh.set_pixel(light[0], light[1], 255, 0, 105)
    uh.show()
    return light

def light_off(light):
    """ turn the specified pixel back to green """
    uh.set_pixel(light[0], light[1], 0, 255, 0)
    uh.show()

def random_lights(num=5):
    """ pick num pixels from the tree and turn them red """
    lights = []
    while True:
        lights.append(light_on())
        time.sleep(0.5)
        if len(lights) > num:
            random.shuffle(lights)
            off = lights.pop()
            light_off(off)
            time.sleep(0.5)

def setup_tree():
    """ light up the static parts """
    uh.rotation(270)
    light_trunk()
    light_tree()
    light_star()


# light up tree, then do the fairy lights

setup_tree()
while True:
    random_lights()
