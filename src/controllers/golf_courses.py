from database.db import db

def get_all_courses():
    sql = "SELECT id, name FROM Courses ORDER BY name"
    return db.session.execute(sql).fetchall()
