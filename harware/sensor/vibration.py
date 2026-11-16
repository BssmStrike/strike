import RPi.GPIO as GPIO
import time

VIBRATION_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_PIN, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(VIBRATION_PIN, GPIO.HIGH)
        print("진동 ON")
        time.sleep(1)

        GPIO.output(VIBRATION_PIN, GPIO.LOW)
        print("진동 OFF")
        time.sleep(1)

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    GPIO.output(VIBRATION_PIN, GPIO.LOW)
    GPIO.cleanup()
