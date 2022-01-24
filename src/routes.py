from flask import render_template, request, session, redirect
from app import app
from controllers import golf_courses, users

@app.route("/")
def index():
    return render_template("index.html")

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
        password = request.form["password"]
        username = request.form["username"]
        if users.login(username, password):
            session["username"] = username
            return redirect("/")
        return render_template("login.html", error="Invalid username or password")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.signup(username, password):
            return redirect("/")
        return render_template("signup.html", error="Invalid username or password")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")