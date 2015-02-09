"""
Dice Clock for Raspberry Pi with added UnicornHat

displays the time split between four dice - two for hours, two for minutes

"""
import unicornhat as uh
import time
import datetime

class DiceClock(object):
    """ tick tock, let's make a clock """

    zero = []
    one = [[1, 1]]
    two = [[0, 0], [2, 2]]
    three = two + one
    four = two + [[0, 2], [2, 0]]
    five = four + one
    six = four + [[1, 0], [1, 2]]
    seven = six + one
    eight = six + [[0, 1], [2, 1]]
    nine = eight + one

    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    def __init__(self):
        self.tick()

    def light_number(self, number, position):
        """
        light up a given number in the specified position, offset from top right
        """
        for [x, y] in number:
            uh.set_pixel(x+position[0], y+position[1], 183, 0, 255)
            uh.show()

    def show_time(self):
        """ split the current time into parts and light it up """
        hour = str(datetime.datetime.now().strftime("%H"))
        minute = str(datetime.datetime.now().strftime("%M"))

        hour1 = int(hour[0])
        hour2 = int(hour[1])
        minute1 = int(minute[0])
        minute2 = int(minute[1])

        self.light_number(self.numbers[hour1], [0, 5])
        self.light_number(self.numbers[hour2], [0, 0])
        self.light_number(self.numbers[minute1], [5, 5])
        self.light_number(self.numbers[minute2], [5, 0])

    def tick(self):
        """ tick tock - update every minute """
        uh.rotation(270)
        while True:
            self.show_time()
            time.sleep(60)
            uh.off()

if __name__ == "__main__":
    clock = DiceClock()
