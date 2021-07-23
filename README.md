# RaspberryPi_Python
### 리눅스 기반 라즈베리파이 파이썬 예제 코드 리포지토리입니다.

---------

- [풀업, 풀다운 회로 구현](https://andjjip.tistory.com/241?category=876593)
- [부저 센서를 이용한 출력과 피아노 구현](https://andjjip.tistory.com/240?category=876593)
- [PWM, 초음파센서를 활용한 후방감지센서 구현](https://andjjip.tistory.com/242?category=876593)
- [Flask를 활용한 gpio 제어](https://andjjip.tistory.com/243?category=876593)
- [Cron식과 Sqlite](https://andjjip.tistory.com/244?category=876593)

--------

## 실습 : IoT 프로젝트
#### 라즈베리파이와 센서를 Flask를 이용해 제어하기 : 웹의 각 버튼을 클릭하면 센서를 제어할 수 있는 프로그램 구현 <br>
1. LED on/off : 버튼 클릭할때마다 on, off 제어 <br>
2. LED 무드등(밝기 조절) : 버튼 클릭할때마다 점점 밝아지고, 점점 어두워지도록 구현 <br>
3. 부저센서출력 : 버튼 클릭하면 도레미파솔라시 부저센서 출력 <br>
4. 초음파센서   : 버튼 클릭하면 10번 측정후에 최소거리값을 웹에 출력 <br>

<p align = "center" >
 <img src = "https://github.com/SeoDongWoo1216/RaspberryPi_Python/blob/main/Resultimage/IoT%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EC%8B%A4%ED%96%89%ED%99%94%EB%A9%B4.gif")
</p>
  
[제어소스](https://github.com/SeoDongWoo1216/RaspberryPi_Python/blob/main/EmbededTest/alltest.py) <br>
[html소스](https://github.com/SeoDongWoo1216/RaspberryPi_Python/blob/main/EmbededTest/templates/index.html) <br>

--------

## 소스 분석

### Flask 라이브러리 사용
- python -m pip install --upgrade flask 를 통해 설치
- Flask를 활용하면 웹에서 데이터를 받아올 수 있다.
- 장식자를 활용하여 URL 연결에 활용되고, 다음 행의 함수부터 장식자가 적용된다.
  
```Python
from flask import Flask
app = Flask(__name__)

@app.route('/')   # 맨 앞에 @는 장식자(decorator)로, 함수 코드를 바꾸지 않아도 장식자 안의 내용만 바꿔서 함수의 동작을 조절할 수 있다.
                  # ('/') 에서 주소 뒤에 '/매개변수' 을 이용하면 매개변수에 해당되는 함수가 실행된다.
def home():
   return render_template("index.html")  # 처음 실행했을때 index.html 웹이 로드된다.

if __name__ == "__main__":
    app.run()
```
-------
  
### GPIO Setting
- GPIO.setmode(GPIO.BCM) : 핀 번호를 GPIO모듈 번호로 사용 / (GPIO.BOARD) : 핀 번호를 보드번호를 참조
- GPIO.setup(Pin,GPIO.IN or OUT) : 핀 번호에서 전류를 보내는지 받는지 설정
- GPIO.PWM(Pin,Frequency) : 초당 펄스의 주파수를 유지한 채, 펄스의 길이를 변화시킴 (출력 조절)
  
<br>
  
-------
  
## LED Control
- ON / OFF 버튼을 활용해 LED ON/OFF 제어
- POST를 통해 value 전달
- request.form['led']로 ON/OFF에 대한 값을 받는다.
  
<img src = "https://github.com/SeoDongWoo1216/RaspberryPi_Python/blob/main/Resultimage/LED_Control.PNG" >
  
#### - Python
```python
# LED on, off 버튼으로 LED 제어
@app.route('/data/led', methods= ['POST'])
def led():
 data = request.form['led']
 if data == "on":
    GPIO.output(ledonoff, 1)
 elif data == "off":
    GPIO.output(ledonoff, 0)
 return home() 
```
  
#### - HTML
```HTML
<h1>LED ON OFF</h1>
   <form action='/data/led' method='post'>
      <button type="submit" name="led" value="on">ON</button>
      <button type="submit" name="led" value="off">OFF</button>
   </form>

```

  <br> 

## Mood Lamp Control
- PWM(Pulse Width Modulation : 펄스폭 변조) 방식으로 LED의 밝기를 조절하여 무드등을 구현
- brighter/darker 버튼에 따라 request.form['pwm']에 값이 할당되고, for문으로 ChangeDutyCycle을 이용하여 밝기 조절

<img src = "https://github.com/SeoDongWoo1216/RaspberryPi_Python/blob/main/Resultimage/Mood_Control.PNG">
  
#### - Python
```python
# 무드등의 on 클릭하면 LED가 점점 밝아지고, off를 클릭하면 LED가 점점 어두워진다.
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
```

#### - HTML
```HTML
<h1>PWM LED</h1>
     <form action='/data/ledmood' method='post'>
        <button type="submit" name="pwm" value="+">brighter</button>
        <button type="submit" name="pwm" value="-">darker</button>
     </form>
```
  
<br>


## Buzzer Control
- buzzer 버튼을 클릭했을때 도레미파솔라시 의 음을 출력
- Buzzer 센서에 알맞는 주파수 값을 미리 정적으로 배열에 넣어주고, for문으로 순서대로 출력
<img src = "https://github.com/SeoDongWoo1216/RaspberryPi_Python/blob/main/Resultimage/Buzzer_control.PNG">

#### - Python
```python
# 부저 버튼을 클릭했을시 도레미파솔라시 출력
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
```
  
#### -HTML
```HTML
 <h1>Buzzer</h1>
         <form action='/data/buzz' method='post'>
            <button type="submit" name="buzz" value="on">buzzer</button>
         </form>
```
  <br> 
  
## Ultra Sonic Controler
- 'Measure' 버튼을 클릭하면 초음파센서가 10번을 측정하는데, 10번 중 최소값을 웹에 출력한다.
<img src = "https://github.com/SeoDongWoo1216/RaspberryPi_Python/blob/main/Resultimage/UltraSonic_Control.PNG">
  
```python
# 거리를 10번 측정하고 최소값을 웹으로 쏴줍니다
@app.route('/data/ultra', methods = ['POST'])
def Ultra():
   try:
      global min
      min = 700.0
      for _ in range(10):
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
```

#### - HTML
```HTML
<h1>UltraSonic Sensor</h1>
     <form action='/data/ultra' method='post'>
        <h4>{{distance}} cm</h4>
        <button type="submit" name="ultra" value="on">Measure</button>
     </form>
```








