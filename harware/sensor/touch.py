import RPi.GPIO as GPIO
import time

TOUCH_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PIN, GPIO.IN)

while True:
    value = GPIO.input(TOUCH_PIN)
    print(value)
    time.sleep(0.1)
