# 후방감지센서 구현(초음파센서에 물체가 가까워질수록 부저센서에 울리는 빈도가 늘어남)
#-*-coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

triggerPin = 14
echoPin = 4
pinPiezo = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT) # 출력
GPIO.setup(echoPin, GPIO.IN)     # 입력
GPIO.setup(pinPiezo, GPIO.OUT)

Alert = 400
Buzz = GPIO.PWM(pinPiezo, 440)

try:
   while True:
      #구형파 발생
      GPIO.output(triggerPin, GPIO.LOW)  # 10마이크로s 동안 초음파를 쏴야함
      time.sleep(0.00001)  # 기초단위가 1초라서 10마이크로는 10의 마이너스 5승
      GPIO.output(triggerPin, GPIO.HIGH)

      #시간측정
      while GPIO.input(echoPin) == 0:  # 펄스 발생
         start = time.time()
      while GPIO.input(echoPin) == 1:  # 펄스 돌아옴
         stop = time.time()
      rtTotime = stop - start   # 리턴 투 타임 = (end시간 - start시간)

      distance = rtTotime * (34000 / 2 )
      print("distance : %.2f cm" %distance) # 거리를 출력

      if(distance <= 40 and distance > 25):
         Buzz.start(50)
         Buzz.ChangeFrequency(Alert)
         time.sleep(0.3)
         Buzz.stop()
         time.sleep(0.3)
      elif(distance <= 25 and distance > 10):
         Buzz.start(50)
         Buzz.ChangeFrequency(523)
         time.sleep(0.15)
         Buzz.stop()
         time.sleep(0.1)
      elif(distance <= 10):
         Buzz.start(80)
         Buzz.ChangeFrequency(523)
         time.sleep(0.05)
         Buzz.stop()
         time.sleep(0.05)
      else:
         Buzz.stop()
         time.sleep(0.5)

except KeyboardInterrupt:
   GPIO.cleanup()
