from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", courses=["Paloheinä Golf", "Kullo Golf", "Keimola Golf Club"])

@app.route("/courses")
def courses():
    pass

@app.route("/course/<int:id>")
def course(id):
    pass