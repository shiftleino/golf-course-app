from database.db import db

def add_review(data):
    sql = """
    INSERT INTO Reviews (user_id, course_id, rating, comment, sent_at)
    VALUES (:user_id, :course_id, :rating, :comment, :sent_at);
    """
    db.session.execute(sql, {"user_id": data.user_id, "course_id": data.course_id, "rating": int(data.rating), "comment": data.comment, "sent_at": data.sent_at})
    db.session.commit()

def get_reviews():
    sql = """
    SELECT id, rating, comment, sent_at
    FROM Reviews;
    """
    result = db.session.execute(sql).fetchall()
    return result

def remove_review(review_id):
    sql = """
    DELETE FROM Reviews WHERE id=:review_id;
    """
    db.session.execute(sql, {"review_id": review_id})
    db.session.commit()