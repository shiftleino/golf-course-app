from flask import render_template, request
from app import app
from controllers import golf_courses

@app.route("/")
def index():
    return render_template("index.html", courses=["Paloheinä Golf", "Kullo Golf", "Keimola Golf Club"])

@app.route("/courses")
def courses():
    all_courses = golf_courses.get_all_courses()
    return render_template("courses.html", courses=all_courses)

@app.route("/course/<int:id>")
def course(id):
    return f"{id}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        pw = request.form["password"]
        username = request.form["username"]
        return render_template("index.html", username=username)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return render_template("signup.html") 