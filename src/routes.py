from flask import render_template, request, session, redirect
from app import app
from controllers import golf_courses, users, reviews

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
    order = "name"
    if len(request.args) == 1:
        order = request.args["sorting"]
    all_courses = golf_courses.get_basic_info(order)
    return render_template("courses.html", courses=all_courses, role=session["user_role"])

@app.route("/courses/<int:course_id>", methods=["GET", "POST"])
def course(course_id):
    if request.method == "GET":
        users.require_login()
        basic_data = golf_courses.get_course_info(course_id)
        location_data = golf_courses.get_location_info(course_id)
        price_data = golf_courses.get_price_info(course_id)
        return render_template("course.html", basic_info=basic_data, location_info=location_data, price_info=price_data, role=session["user_role"], course=course_id)
    elif request.method == "POST":
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
            golf_courses.change_info(data, course_id)
            return redirect(f"/courses/{course_id}")
        except:
            users.require_login()
            basic_data = golf_courses.get_course_info(course_id)
            location_data = golf_courses.get_location_info(course_id)
            price_data = golf_courses.get_price_info(course_id)
            return render_template("course.html", error="Updating the information failed. Check that the values make sense.", basic_info=basic_data, location_info=location_data, price_info=price_data, role=session["user_role"], course=course_id)

@app.route("/courses/<int:course_id>/reviews", methods=["GET", "POST"])
def review(course_id):
    users.require_login()
    if request.method == "GET":
        name = golf_courses.get_course_info(course_id).name
        all_reviews = reviews.get_reviews()
        return render_template("reviews.html", reviews=all_reviews, name=name, role=session["user_role"])
    elif request.method == "POST":
        users.check_csrf()
        comment = request.form["comment"]
        rating = request.form["rating"]
        user_id = session["user_id"]
        if rating.isnumeric() and comment != "":
            data = {
                "user_id": user_id,
                "course_id": course_id,
                "comment": comment,
                "rating": rating,
            }
            reviews.add_review(data)
        return redirect(f"/courses/{course_id}")

@app.route("/courses/<int:course_id>/reviews/<int:review_id>", methods=["POST"])
def remove_review(course_id, review_id):
    users.require_role(1)
    users.check_csrf()
    reviews.remove_review(review_id)
    return redirect(f"/courses/{course_id}")

@app.route("/remove/<int:course_id>", methods=["POST"])
def remove(course_id):
    users.require_role(1)
    users.check_csrf()
    golf_courses.delete_course(course_id)
    return redirect("/courses")

@app.route("/courses/<int:course_id>/prices", methods=["POST"])
def add_greenfee(course_id):
    users.require_role(1)
    users.check_csrf()
    key = request.form["name"]
    value = request.form["price"]
    if key and value and value.isnumeric():
        golf_courses.add_greenfee(course_id, key, value)
    return redirect(f"/courses/{course_id}")

@app.route("/courses/<int:course_id>/prices/<int:price_id>", methods=["POST"])
def remove_greenfee(course_id, price_id):
    users.require_role(1)
    users.check_csrf()
    golf_courses.delete_greenfee(price_id)
    return redirect(f"/courses/{course_id}")

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