import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Set GPIO to pin numbering
pir = 23 #Assign pin 8 to PIR
led = 21 #Assign pin 10 to LED
GPIO.setup(pir, GPIO.IN) #Setup GPIO pin PIR as input
GPIO.setup(led, GPIO.OUT) #Setup GPIO pin for LED as output
print ("Sensor initializing . . .")
time.sleep(2) #Give sensor time to startup
print ("Active")
print ("Press Ctrl+c to end program")
GPIO.output(led, GPIO.HIGH)
time.sleep(4)
GPIO.output(led, GPIO.HIGH)
try:
  while True:
    if GPIO.input(pir) == True: #If PIR pin goes high, motion is detected
      print ("Motion Detected!")
      GPIO.output(led, GPIO.HIGH) #Turn on LED
      print ("led on!")
      time.sleep(4) #Keep LED on for 4 seconds
      #GPIO.output(led, GPIO.LOW) #Turn off LED
      #time.sleep(0.1)
      #some chanfes

except KeyboardInterrupt: #Ctrl+c
  pass #Do nothing, continue to finally

#finally:
  #GPIO.output(led, False) #Turn off LED in case left on
GPIO.cleanup() #reset all GPIO
print ("Program ended")