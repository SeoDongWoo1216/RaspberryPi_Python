# 웹에 접속했을때 Hello Flask!! 가 출력
from flask import Flask

app = Flask(__name__)   #__name__ 이름을 이용한 Flask객체생성

@app.route('/')
def hello():            #뷰함수
   return "Hello Flask!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port = "8080")
