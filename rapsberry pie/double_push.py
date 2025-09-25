import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
'''but1 = 9
but2 = 10
GPIO.setup(but1, GPIO.IN)
GPIO.setup(but2, GPIO.IN)
while True:
    if GPIO.input(but1) and GPIO.input(but1):
        GPIO.output(leds, 1)
'''