import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
but1 = 9
but2 = 10
GPIO.setup(but1, GPIO.IN)
GPIO.setup(but2, GPIO.IN)
num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.8
while True:
    if GPIO.input(but1):
        num += 1
        nim = min(255, num)
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(but2):
        num -= 1
        num = max(0, num)
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))