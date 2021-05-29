import RPi.GPIO as GPIO
import time

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
   while True:
      GPIO.output(led,True)
      time.sleep(1)
      GPIO.output(led,False)
      time.sleep(1)

except KeyboardInterrupt:
   GPIO.cleanup()
