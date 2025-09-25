import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
state = 0
led = 26
GPIO.setup(led, GPIO.OUT)
period = 0.5
while True:
    GPIO.output(led, state)
    state = not state
    time.sleep(period)

cleanup()