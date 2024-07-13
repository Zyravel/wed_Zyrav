from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():
    return "WTF!"



@app.route("/user/<x>")
def hx(x):
    return f'hellow, {x}'

app.run()