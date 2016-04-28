"""
playing around with an RGB LED, breadboard, and some jumper cables
"""

from gpiozero import RGBLED
from time import sleep

# GPIO pin numbers
led = RGBLED(red=17, green=27, blue=22)

led.on()
sleep(5)
led.off()

"""
led.value = (0, 1, 0)  # full green
sleep(1)
led.value = (1, 0, 1)  # magenta
sleep(1)
led.value = (1, 1, 0)  # yellow
sleep(1)
led.value = (0, 1, 1)  # cyan
sleep(1)
led.value = (1, 1, 1)  # white
sleep(1)

led.value = (0, 0, 0)  # off
"""

# cycle through a rainbow (predictable...)
while True:
        led.red = 1
        sleep(0.5)
        led.green = 1
        sleep(0.5)
        led.red = 0
        sleep(0.5)
        led.blue = 1
        sleep(0.5)
        led.green = 0
        sleep(0.5)
        led.red = 1
        sleep(0.5)
        led.blue = 0
