# 풀다운회로에서 스위치를 누를때마다 print가 출력
# -*- coding: utf-8-*-
import RPi.GPIO as GPIO     # 모듈 RPi.GPIO를 사용하겠다는 뜻임(as로 명명가능)
import time                 # time.sleep을 쓰기위해 import로 선언

switch1 = 6                 # 입력핀 설정

GPIO.setmode(GPIO.BCM)      # BCM 모드 사용(pin은 BCM으로 쓰겠다는 뜻)
GPIO.setup(switch1, GPIO.IN) # 핀모드(입력) (출력으로 사용하려면 GPIO.OUT으로 사용)

try:
   while True:
      if GPIO.input(switch1) == True:
         print("1번Pushed")
         time.sleep(0.3) # 이거 없으면 스위치눌렀을때 Pushed가 주르륵나옴
                   # 스위치를 눌렀을때의 진동때문에 주르륵나오는데
                   # 진동구간을 잠시 무시하고 눌러지는 순간의 데이터만 읽겠다는 뜻

except KeyboardInterrupt:
   GPIO.cleanup()



