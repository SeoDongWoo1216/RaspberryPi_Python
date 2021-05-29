# 숫자키를 누르면 누르자마자 부저센서에서 그 숫자에 맞는 계이름 출력(최종버전임)
# -*-coding: utf-8-*-

import sys, termios, tty, os, time
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

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)       # 런타임워닝 무시해줌(scanf할때처럼)
GPIO.setup(pinPiezo, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)

def buzz_Freq(Piano):
   #print("주파수 : %d 입력" %Piano)
   Buzz.ChangeFrequency(Piano)
   time.sleep(0.2)
   Buzz.stop()

def getch():
       fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)

   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

   try:
   while True:
      char = getch()
      Buzz.start(90)
      if(char == '1'):
         print("도")
         buzz_Freq(C)
      elif(char == '2'):
         print("레")
         buzz_Freq(D)
      elif(char == '3'):
         print("미")
         buzz_Freq(E)
      elif(char == '4'):
         print("파")
         buzz_Freq(F)
      elif(char == '5'):
         print("솔")
         buzz_Freq(G)
      elif(char == '6'):
         print("라")
         buzz_Freq(A)
      elif(char == '7'):
         print("시")
         buzz_Freq(B)
      elif(char == '8'):
         print("2옥도")
         buzz_Freq(Cc)
      else:
         exit(0)


except KeyboardInterrupt:
   GPIO.cleanup()

