from src.database.db import db

def add_review(data):
    sql = """
    INSERT INTO Reviews (user_id, course_id, rating, comment, sent_at)
    VALUES (:user_id, :course_id, :rating, :comment, NOW());
    """
    db.session.execute(sql, {"user_id": data["user_id"], "course_id": data["course_id"], "rating": int(data["rating"]), "comment": data["comment"]})
    db.session.commit()

def get_reviews(course_id):
    sql = """
    SELECT id, rating, comment, sent_at
    FROM Reviews
    WHERE course_id=:course_id;
    """
    result = db.session.execute(sql, {"course_id": course_id}).fetchall()
    return result

def remove_review(review_id):
    sql = """
    DELETE FROM Reviews WHERE id=:review_id;
    """
    db.session.execute(sql, {"review_id": review_id})
    db.session.commit()