# testing all the pyGlow stuff
import time
from lib.pyglow import PyGlow

pyglow = PyGlow()

brightness = 50


def colour(colour, brightness):
    """ yeah, I keep failing to spell it wrong """
    pyglow.color(colour, brightness)


def off():
    pyglow.all(0)


def cycleColours(brightness, sleep):
    """ cycle all of each colour """
    """colour('red', brightness)
    time.sleep(sleep)
    colour('orange', brightness)
    time.sleep(sleep)
    colour('yellow', brightness)
    time.sleep(sleep)
    colour('green', brightness)
    time.sleep(sleep)
    colour('blue', brightness)
    time.sleep(sleep)
    colour('white', brightness)"""

    # or
    for i in range(6, 0, -1):  # white is colour 1
        colour(i, brightness)
        time.sleep(sleep)


def cycleColoursR(brightness, sleep):
    for i in range(1, 7):  # white is colour 1
        colour(i, brightness)
        time.sleep(sleep)


def cycleIndiv(brightness, sleep):
    """cycle colours in order, one arm at a time """
    for i in range(1, 19):
        pyglow.set_leds([i], brightness)
        pyglow.update_leds()
        time.sleep(sleep)


def spiral(brightness, sleep):
    """ one by one, 'spiralling' inwards' """
    x = 1
    for i in range(1, 19):
        if x > 18:
            x = x-17
        pyglow.set_leds([x], brightness)
        pyglow.update_leds()
        time.sleep(sleep)
        x += 6


def cycleArms(brightness, sleep):
    pyglow.arm(1, brightness)
    time.sleep(sleep)
    pyglow.arm(2, brightness)
    time.sleep(sleep)
    pyglow.arm(3, brightness)
    time.sleep(sleep)

""" main program - go through all the patterns above on a continuous loop """


def main():
    try:

        while (True):

            cycleColours(brightness, 0.1)
            cycleColours(0, 0.1)

            cycleColoursR(brightness, 0.1)
            cycleColoursR(0, 0.1)

            cycleIndiv(brightness, 0.1)
            cycleIndiv(0, 0.1)

            cycleArms(brightness, 0.1)
            cycleArms(0, 0.1)

            spiral(brightness, 0.2)
            spiral(0, 0.2)

    except KeyboardInterrupt:
        # set all the LEDs to "off" when Ctrl+C is pressed before exiting
        pyglow.lights_off('bye bye')

if __name__ == "__main__":
    main()
