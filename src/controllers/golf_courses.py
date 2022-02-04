from database.db import db

def get_basic_info(order="name"):
    if order == "distance":
        sql = """
        SELECT C.id, C.name, L.distance, (SELECT value AS greenfee FROM CoursePrices WHERE key='Green fee' AND course_id=C.id)
        FROM Courses as C, CourseLocations AS L
        WHERE C.id=L.course_id
        ORDER BY L.distance;
        """
    elif order == "greenfee":
        sql = """
        SELECT C.id, C.name, L.distance, (SELECT value AS greenfee FROM CoursePrices WHERE key='Green fee' AND course_id=C.id)
        FROM Courses as C, CourseLocations AS L
        WHERE C.id=L.course_id
        ORDER BY greenfee;
        """
    else:
        sql = """
        SELECT C.id, C.name, L.distance, (SELECT value AS greenfee FROM CoursePrices WHERE key='Green fee' AND course_id=C.id)
        FROM Courses as C, CourseLocations AS L
        WHERE C.id=L.course_id
        ORDER BY C.name;
        """
    result = db.session.execute(sql).fetchall()
    return result

def get_course_info(course_id):
    sql = """
    SELECT name, holes, link
    FROM Courses
    WHERE id=:id
    """
    result = db.session.execute(sql, {"id": course_id}).fetchone()
    return result

def get_location_info(course_id):
    sql = """
    SELECT address, municipality, distance, drive_time
    FROM CourseLocations
    WHERE course_id=:id
    """
    result = db.session.execute(sql, {"id": course_id}).fetchone()
    return result

def get_price_info(course_id):
    sql = """
    SELECT key, value
    FROM CoursePrices
    WHERE course_id=:id
    """
    result = db.session.execute(sql, {"id": course_id}).fetchall()
    return result

def add_course(data):
    sql = """
    INSERT INTO Courses (name, holes, link)
    VALUES (:name, :holes, :link);
    """
    db.session.execute(sql, {"name": data["name"], "holes": int(data["holes"]), "link": data["link"]})
    sql = """
    SELECT id FROM Courses WHERE name=:name;
    """
    course_id = db.session.execute(sql, {"name": data["name"]}).fetchone()[0]
    sql = """
    INSERT INTO CourseLocations (course_id, address, latitude, longitude, municipality, distance, drive_time)
    VALUES (:id, :address, :lat, :lon, :municipality, :distance, :drive_time);
    """
    db.session.execute(sql, {"id": course_id, "address": data["address"], "lat": float(data["lat"]), "lon": float(data["lon"]), "municipality": data["municipality"], "distance": int(data["distance"]), "drive_time": int(data["drive_time"])})
    db.session.commit()

def delete_course(course_id):
    sql = """
    DELETE FROM Courses WHERE id=:course_id;
    """
    db.session.execute(sql, {"course_id": course_id})
    db.session.commit()