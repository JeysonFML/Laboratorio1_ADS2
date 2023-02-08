from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola Mundo!</p>"

@app.route("/jeyson")
def hello_world():
    return "<p>Hola soy Jeyson!</p>"