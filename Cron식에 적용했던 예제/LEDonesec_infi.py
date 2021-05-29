#! /usr/bin/env python3.7

# cron식에 적용했던 코드
# cron식은 스케줄링을 하게해주는 프로그램임.
# LED가 켜졌다가 꺼졌다가를 무한반복
import RPi.GPIO as GPIO
import time

Led = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT)
num = 10

try:
   while(1):
      GPIO.output(Led, 1)ㅜ무ㅐ
      print("켜집니다")
      time.sleep(0.5)

      GPIO.output(Led, 0)
      print("꺼집니다")
      time.sleep(0.5)

except KeyboardInterrupt:
   print()
   GPIO.cleanup()
