# Blink an LED on GPIO 17: on for one second, off for one second, forever.
from time import sleep

from gpiozero import LED

led = LED(17)

while True:
    # TODO: turn the LED on, wait 1 second, turn it off, wait 1 second
    pass
