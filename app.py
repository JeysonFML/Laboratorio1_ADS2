from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():    
    return "<p>Hello, World!</p>"

@app.route("/juanf")
def hello_juanf():
    return "<p>Hello, Soy Juan Fernando Lopez Bol</p>"

