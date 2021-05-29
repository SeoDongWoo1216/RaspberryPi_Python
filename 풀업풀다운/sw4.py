# 풀다운 회로에서 스위치를 누를때마다 인터럽트를 감지해서 print가 출력되는 코드
# 인터럽트 : 0에서 1이 되는 엣지 구간
#-*-coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switch = 6
flag = False                # bool형 flag 사용

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # 내부풀다운 사용
def swBlink(channel):       # callback 함수
   global flag
   if flag == False:        # flag의 T/F에 따라 인터럽트 결정
      print("interrupt")
      flag = True
   else:
      flag = False

#인터럽터핀에 라이징 신호가 인가되면 콜백함수로 리턴되어 실행
GPIO.add_event_detect(switch, GPIO.RISING, callback=swBlink)

try:
   while True:
      pass

except KeyboardInterrupt:
   print()
   GPIO.cleanup()
