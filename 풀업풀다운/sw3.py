# 스위치를 한번 누르면 LED on, 또 한번 누르면 LED off
# -*- coding: utf-8-*-
import RPi.GPIO as GPIO     # 모듈 RPi.GPIO를 사용하겠다는 뜻임(as로 명명가능)
import time                 # time.sleep을 쓰기위해 import로 선언

switch1 = 6                  # 입력핀 설정
LED = 2
state = 1
GPIO.setmode(GPIO.BCM)      # BCM 모드 사용(pin은 BCM으로 쓰겠다는 뜻)

GPIO.setup(switch1, GPIO.IN) # 핀모드(입력) (출력으로 사용하려면 GPIO.OUT으로 사용)
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, False)

try:
   while True:
      if GPIO.input(switch1) == True:
         print("Pushed")
         if (state == 1):             # 홀수일때 on, 짝수일때 off
            GPIO.output(LED, True)
         else:
            GPIO.output(LED, False)
         time.sleep(0.3)
         state = state + 1            # flag를 홀짝으로 설정했음
         state = state % 2

except KeyboardInterrupt:
   GPIO.cleanup()
