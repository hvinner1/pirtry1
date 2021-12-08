import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
temp= 12
buzzState = False
GPIO.setup(temp, GPIO.IN)

while True:
    buzzState = not buzzState
    print(GPIO.input(temp))
    time.sleep(2)