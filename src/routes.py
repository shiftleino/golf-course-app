from flask import render_template, request, session, redirect
from app import app
from controllers import golf_courses, users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/courses", methods=["GET", "POST"])
def courses():
    users.require_login()
    if request.method == "POST":
        users.check_csrf()
        users.require_role(1)
        try:
            data = {
                "name": request.form["name"],
                "holes": request.form["holes"],
                "link": request.form["link"],
                "address": request.form["address"],
                "lat": request.form["lat"],
                "lon": request.form["lon"],
                "municipality": request.form["municipality"],
                "distance": request.form["distance"],
                "drive_time": request.form["drive_time"]
            }
            golf_courses.add_course(data)
        except:
            all_courses = golf_courses.get_basic_info()
            return render_template("courses.html", courses=all_courses, role=session["user_role"], error="Something went wrong when adding the golf course.")
    all_courses = golf_courses.get_basic_info()
    return render_template("courses.html", courses=all_courses, role=session["user_role"])

@app.route("/courses/<int:course_id>", methods=["GET", "POST"])
def course(course_id):
    users.require_login()
    basic_data = golf_courses.get_course_info(course_id)
    location_data = golf_courses.get_location_info(course_id)
    price_data = golf_courses.get_price_info(course_id)
    return render_template("course.html", basic_info=basic_data, location_info=location_data, price_info=price_data)

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
    users.logout()
    return redirect("/")