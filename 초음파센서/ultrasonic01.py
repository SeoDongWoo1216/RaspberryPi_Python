# 초음파센서에 물체를두면 초음파센서와 물체와의 거리를 무한으로 출력(컨트롤 C누르면 종료)
#-*-coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

triggerPin = 14
echoPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT) # 출력
GPIO.setup(echoPin, GPIO.IN)     # 입력

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

      # 거리 = 시간 * 속력
      # 이때 소리의  속력은 340m/s인데 cm로 단위를 바꿔줘야함=> 34000 cm/s
      # 그리고 340m/s 는 왕복속도라서 편도로 봐야하니 나누기 2를 해줘야함
      distance = rtTotime * (34000 / 2 )
      print("distance : %.2f cm" %distance) # 거리를 출력
      time.sleep(1)  # 1초마다 받아옴

except KeyboardInterrupt:
   GPIO.cleanup()
