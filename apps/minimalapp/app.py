from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, flask!"


@app.route("/hello/<name>")
def hello(name):
    return f"Hello,{name}!"
