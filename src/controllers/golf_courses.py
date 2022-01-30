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