# 프로그램을 실행하면 사용중이라고 잠재적위험을 감지하니 gpio핀들을 초기화시켜주는 코드임

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.cleanup()
