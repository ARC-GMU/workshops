# Blink an LED on GPIO 17: on for one second, off for one second, forever.
from time import sleep

from gpiozero import LED

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
