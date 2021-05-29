# 0~100의 숫자를 입력받으면 그 숫자에따른 LED의 밝기를 조절할 수 있는 코드 구현
#-*-coding: utf-8-*-

import RPi.GPIO as GPIO

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

p = GPIO.PWM(ledPin, 255)

p.start(0)

while True:
   d = input("Enter Brightness(0 to 100) : ")
   duty = int(d)

   if(duty == 100):
      p.stop()
      GPIO.cleanup()
      break
   else:
      p.ChangeDutyCycle(duty)
