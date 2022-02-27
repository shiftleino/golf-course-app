from database.db import db

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

def get_average_rating(course_id):
    sql = """
    SELECT CAST(AVG(rating) AS DECIMAL(4, 2))
    FROM Reviews
    WHERE course_id=:course_id;
    """
    average = db.session.execute(sql, {"course_id": course_id}).fetchone()[0]
    return average

def get_count_reviewers(course_id):
    sql = """
    SELECT COUNT(Distinct user_id)
    FROM Reviews
    WHERE course_id=:course_id;
    """
    count = db.session.execute(sql, {"course_id": course_id}).fetchone()[0]
    return count
