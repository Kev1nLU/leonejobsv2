from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello  {escape(name)}, Welcome!!'

@app.route('/user/<int:userid>')
def userid(userid):    
    return f'Hello user number#: {escape(userid)}'