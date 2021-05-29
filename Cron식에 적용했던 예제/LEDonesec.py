# LED가 10번동안 켜졌다가 꺼지는 것을 반복
import RPi.GPIO as GPIO
import time

Led = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT)
num = 10

try:
   while(num > 0):
      GPIO.output(Led, 1)
      print("켜집니다 : %d" %num)
      time.sleep(0.5)

      GPIO.output(Led, 0)
      print("꺼집니다")
      time.sleep(0.5)
      num = num - 1

except KeyboardInterrupt:
   GPIO.cleanup()
