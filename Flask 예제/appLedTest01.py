# 웹에 접속했을때 주소창에 /led/on  또는 /led/off 또는 /led/clean 을 입력했을때 LED의 변화를 관찰하는 예제
# => 일일이 정해진 주소를 입력해야되서 정적라우팅이라고 부름

from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def flask():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(ledPin, GPIO.OUT)
   GPIO.output(ledPin, 0)
   return "Hello Flask"

@app.route('/led/on')
def ledOn():
   GPIO.output(ledPin, 1)
   return "<h1> LED ON </h1> "

@app.route('/led/off')
def LedOff():
   GPIO.output(ledPin, 0)
   return "<h1> LED OFF </h1>"

@app.route('/led/clean')
def clean():
   GPIO.cleanup()        #핀을 클린시키는 코드
   return "<h1> GPIO Clean </h1>"

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port = "8080")
