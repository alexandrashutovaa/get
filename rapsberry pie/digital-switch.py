import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
state = 0
led = 26
GPIO.setup(led, GPIO.OUT)
button = 13
GPIO.setup(button, GPIO.IN)
while True:
    if GPIO.input(button):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)