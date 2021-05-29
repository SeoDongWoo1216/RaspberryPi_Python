# 풀다운회로에서 1개의 스위치를 눌렀을때 LED on, 한번 더 눌렀을때 LED off 되는 코드 구현
# sw3과는 다르게 인터럽트를 감지하기때문에 time.sleep이 필요없고, 홀짝으로 감지하던 flag를 bool형으로 구현하였다.
#-*-coding: utf-8-*-
import RPi.GPIO as GPIO
import time

switch = 6
LED = 2
flag = False                    # 홀짝으로했던 sw3와는 다르게 bool형 flag 사용

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # 내부풀다운 사용
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)         # 처음 실행했을때는 LED를 꺼줌

def swBlink(channel):           # callback 함수
   global flag
   if flag == False:          
      GPIO.output(LED, True)
      print("interrupt")
      flag = True

   else:
      flag = False 
      GPIO.output(LED, False)


#인터럽터핀에 라이징 신호가 인가되면 콜백함수로 리턴되어 실행
GPIO.add_event_detect(switch, GPIO.RISING, callback=swBlink)

try:
   while True:
      pass

except KeyboardInterrupt:
   print()
   GPIO.cleanup()
