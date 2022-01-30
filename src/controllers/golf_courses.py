from database.db import db

def get_all_courses():
    sql = "SELECT id, name FROM Courses ORDER BY name"
    result = db.session.execute(sql).fetchall()
    return result

def get_basic_info():
    sql = """
    SELECT C.id, C.name, L.distance, (SELECT value AS greenfee FROM CoursePrices WHERE key='Green fee' AND course_id=C.id)
    FROM Courses as C, CourseLocations AS L
    WHERE C.id=L.course_id;
    """
    result = db.session.execute(sql).fetchall()
    return result