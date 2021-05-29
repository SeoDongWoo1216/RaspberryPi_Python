# 파일명 : alltest.py
# 지금까지했던 센서들을 웹으로 제어 => 웹의 각 버튼을 클릭하면 센서를 제어할 수 있는 프로그램 구현
# 1. LED on/off
# 2. LED 무드등(밝기 조절)
# 3. 부저센서출력
# 4. 초음파센서

from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

ledonoff = 21
ledMood = 3
buzzer = 16
triggerPin = 14
echoPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledonoff, GPIO.OUT)   # 21
GPIO.setup(ledMood, GPIO.OUT)    # 3
GPIO.setup(buzzer, GPIO.OUT)     # 16
GPIO.setup(triggerPin, GPIO.OUT) # 14
GPIO.setup(echoPin, GPIO.IN)     # 4

p = GPIO.PWM(ledMood, 255)
Buzz = GPIO.PWM(buzzer, 440)

global i
i = 0


@app.route('/')
def home():
   return render_template("index.html")


@app.route('/data/led', methods= ['POST'])
def led():
   data = request.form['led']
   if data == "on":
      GPIO.output(ledonoff, 1)
   elif data == "off":
      GPIO.output(ledonoff, 0)
   return home()


@app.route('/data/ledmood', methods = ['POST'])
def ledmood():
   global i
   data = request.form['pwm']
   p.start(0)
   try:
      if data == "+":
         for i in range(20):
            p.ChangeDutyCycle(5*i)
            time.sleep(0.1)
      elif data == "-":
         for i in reversed(range(20)):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)

   except KeyboardInterrupt:
      print()
      GPIO.cleanup()
   return home()


@app.route('/data/buzz', methods = ['POST'])
def Buzzsong():
   data = request.form['buzz']
   Melody = [261, 294, 329, 349, 440, 493, 523]
   try:
      if data == "on":
         Buzz.start(90)
         for i in range(0, len(Melody)):
            Buzz.ChangeFrequency(Melody[i])
            time.sleep(0.3)
         Buzz.stop()
         time.sleep(1)
   except KeyboardInterrupt:
      print()
      GPIO.cleanup()

   return home()


# 거리를 10번 측정하고 최소값을 웹으로 쏴줍니다
@app.route('/data/ultra', methods = ['POST'])
def Ultra():
   try:
      global min
      min = 700.0
      for _ in range(10):   # 현수님꺼 참고했습니다
         GPIO.output(triggerPin, GPIO.LOW)
         time.sleep(0.00001)
         GPIO.output(triggerPin, GPIO.HIGH)

         while GPIO.input(echoPin) == 0:
            start = time.time()
         while GPIO.input(echoPin) == 1:
            stop = time.time()

         rtTotime = stop - start

         distance = rtTotime * ( 34000 / 2 )
         distance = round(distance, 2)
         print("distance : %.2f cm" %distance)
         time.sleep(0.2)

         if min > distance:
            min = distance

   except KeyboardInterrupt:
      print()
      GPIO.cleanup()

   return render_template("index2.html", distance = min)   # 최소값을 웹에 전달


@app.route('/data/clean', methods = ['POST'])
def clean():
   data = request.form['led']
   try:
      if data == "clean":
         print()
         GPIO.cleaup()
      elif data == "set":
         print("세팅")
   except:
      pass

   return home()


if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = '8080')
