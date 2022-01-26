from flask import Flask
from gevent import pywsgi
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return """<h2>主页</h2>
              <a href="/login">登录</a>
           """

@app.route('/login',methods=['GET'])
def signin_form():
    return """<form action="/loginstatus" method="post">
                <p>用户名：<input name="username"></p>
                <p>密  码：<input name="password"></p>
                <p><button type="submit">登录</button></p>
              </form>
            """

@app.route("/loginstatus",methods=["post"])
def signin():
    if request.form['username']=="username1" and request.form["password"]=="password1":
        return """<h4>Hello,<a id="user" href="/dashboad">username1</a>!</h4>
                  <a href="/logout">登出</a>
               """
    return "<h4>用户名或密码错误！</h4>"

server = pywsgi.WSGIServer(('0.0.0.0', 12345), app)
server.serve_forever()

if __name__ == "__main__":
    # http://localhost:5001
    app.run(port=5001,debug=False)



























