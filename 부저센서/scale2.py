# 부저센서에 노래출력 => 실패
# -*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time

O = 1
C = 261 # 도
D = 293 # 레
E = 329 # 미
F = 349 # 파
Ff = 370 # 파샵
G = 391 # 솔
A = 440 # 라
B = 493 # 시
Cc = 523 # 2옥도

pinPiezo = 21

#Melody = [G,O,G,O,A,O,A,O, G,O,G,O,E,O,G,O,G,O,E,O,E,O,D,O,O,G,O,G,O,A,O,A,O,G,O,G,O,E,O,G,O,E,O,D,O,E,O,C]
#Melody = [B,F,B,F, G,D,G,D, A,E,A,E, D,A,D,A]

Melody = [G,G,A,A,G,G,E,G,G,E,E,D,G,G,A,A,G,G,E,G,E,D,E,C]
#Melody = [131, 147, 165, 174, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)

try:
   while True:
      Buzz.start(50)
   while True:
          Buzz.start(50)
      for i in range(0, len(Melody)):
         Buzz.ChangeFrequency(Melody[i])
         time.sleep(0.3)
      Buzz.stop()
      time.sleep(1)

except KeyboardInterrupt:
   GPIO.cleanup()