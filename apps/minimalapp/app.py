from flask import Flask, current_app, g, render_template, request, url_for

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


# url_for(理解のための記述)
with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/jou?page=1
    print(url_for("show_name", name="jou", page="1"))


# コンテキスト(仕組み理解のための記述)
# アプリケーションコンテキスト
ctx = app.app_context()
ctx.push()

print(current_app.name)

# リクエストコンテキスト
g.connection = "connection"
print(g.connection)

with app.test_request_context("/users?updated=true"):
    print(request.args.get("updated"))
