from flask import render_template, request
from app import app

@app.route("/")
def index():
    return render_template("index.html", courses=["Paloheinä Golf", "Kullo Golf", "Keimola Golf Club"])

@app.route("/courses")
def courses():
    return "The golf courses in Uusimaa, Finland"

@app.route("/course/<int:id>")
def course(id):
    return f"{id}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        pass

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html") 