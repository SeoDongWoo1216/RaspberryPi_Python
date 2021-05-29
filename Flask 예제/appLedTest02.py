# 01에서 주소창의 사이트를 정해진 값이아니라 아무 값이나 받았을때도 해당되는 페이지가 나오도록 구현
# => 아무값이나 받아도되기때문에 동적라우팅이라고 부름

from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(ledPin, GPIO.OUT)


@app.route('/')
def ledFlask():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(ledPin, GPIO.OUT)
   return "<h1> LED Control WepPage </h1>"


@app.route('/led/<state>')  # /이 매개변수로 와야함
def led(state):
   if(state == 'on'):
      GPIO.output(ledPin, 1)  # LED 키고
   else:
      GPIO.output(ledPin, 0)  # LED 끄고
   return ("<h1> LED %s </h1>" %state)


@app.route('/led/clean')
def clean():
   GPIO.output(ledPin, GPIO.LOW)
   GPIO.cleanup()
   return "<h1> GPIO Clean!! </h1>"

if __name__ == "__main__":
       app.run(host = "0.0.0.0", port = "8080")
