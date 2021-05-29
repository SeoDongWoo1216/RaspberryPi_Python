# 부저센서에 도레미파솔라시도 출력
# -*-coding: utf-8-*-

import RPi.GPIO as GPIO
import time


pinPiezo = 16
Melody = [261, 294, 329, 349, 392, 440, 493, 523]
#Melody = [131, 147, 165, 174, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)

try:
   while True:
      Buzz.start(50)
      for i in range(0, len(Melody)):
         Buzz.ChangeFrequency(Melody[i])
         time.sleep(0.3)
      Buzz.stop()
      time.sleep(1)

except KeyboardInterrupt:
   GPIO.cleanup()
