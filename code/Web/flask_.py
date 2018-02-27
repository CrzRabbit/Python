from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return b'<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_from():
    return open('signin_from.html').read()

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'admin':
        return b'<h1>Hello, admin!</h1>'
    return b'<h3>Bad userinfo.</h3>'

if __name__ == '__main__':
    app.run()