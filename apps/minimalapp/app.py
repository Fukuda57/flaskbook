from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, flask!"


@app.route("/hello/<name>", endpoint="hello-endpoint")
def hello(name):
    return f"Hello,{name}!"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/jou?page=1
    print(url_for("show_name", name="jou", page="1"))
