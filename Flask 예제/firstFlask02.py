# 처음 페이지에서 name, age, job, about을 주소창에치면 그에맞는 해당페이지에 값을 리턴해서 웹에 출력
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   return "Hello Flask"

@app.route('/name')
def name():
   return "<h1> My name is SeoDongWoo <h1>"

@app.route('/age')
def age():
   return "<h2> My age is 27 <h2>"

@app.route('/job')
def job():
   return "<h3> My job is developer <h3>"

@app.route('/about')
def about():
   return "<h1> My name is SeoDongWoo <h1> <h2> My age is 27 years old <h2> <h3> my job is delopver <h3>"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port = "8080")
