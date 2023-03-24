from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello, this is the index page!"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {escape(name)}, Welcome to this page!!"