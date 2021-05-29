# 1번스위치를 누르면 LED On, 2번 스위치를 누르면 LED off
# 1, 2번 스위치의 pin에 input이 들어가고
# 스위치 input에따라 LED pin의 output이 달라짐

# -*- coding: utf-8-*-
import RPi.GPIO as GPIO     # 모듈 RPi.GPIO를 사용하겠다는 뜻임(as로 명명가능)
import time                 # time.sleep을 쓰기위해 import로 선언

switch1 = 6                  # 입력핀 설정
switch2 = 5
LED = 2
GPIO.setmode(GPIO.BCM)      # BCM 모드 사용(pin은 BCM으로 쓰겠다는 뜻)

GPIO.setup(switch1, GPIO.IN) # 핀모드(입력) (출력으로 사용하려면 GPIO.OUT으로 사용)
GPIO.setup(switch2, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)
try:
   while True:
      if GPIO.input(switch1) == True:
         print("1번Pushed=>LED On")
         GPIO.output(LED, True)
         time.sleep(0.3)
      elif GPIO.input(switch2) == True:
         print("2번Pushed=>LED Off")
         GPIO.output(LED, False)
         time.sleep(0.3)

except KeyboardInterrupt:
   GPIO.cleanup()
