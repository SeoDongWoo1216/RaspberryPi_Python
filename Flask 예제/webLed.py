# 웹에서 버튼을 눌렀을때 LED를 제어하는 코드
from flask import Flask, request, render_template # 3개를 import
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def home():
   return render_template("index.html")   # 메인페이지에서 index.html을 호출


@app.route('/data', methods = ['POST'])
def data():
   data = request.form['led'] # led라는 이름을통해 form에 집어넣은걸
                              # data에 저장

   if(data == 'on'):
      GPIO.output(ledPin, 1)  # LED 켜줌
      return home()
   elif(data == 'off'):
      GPIO.output(ledPin, 0)  # LED 끔
      return home()
   elif(data == 'clean'):
      GPIO.cleanup()
      return home()
   elif(data == 'Restart'):
      try:
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(ledPin, GPIO.OUT)
         return home()
      except:
         print("이미 핀이 설정되있습니다")
         return home()

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = '8080')
