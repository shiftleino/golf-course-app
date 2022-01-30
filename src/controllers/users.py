from werkzeug.security import check_password_hash, generate_password_hash
from flask import session, abort
from database.db import db

def signup(username, password):
    if len(username) < 3 or len(password) < 3:
        return False
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO Users (username, password, role) VALUES (:username, :password, 0)"
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
        return True
    except:
        return False

def login(username, password):
    sql = "SELECT id, password, role FROM Users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["user_id"] = user.id
            session["username"] = username
            session["user_role"] = user.role
            return True
        return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["user_role"]

def require_login():
    user_id = session.get("user_id", 0)
    if user_id == 0:
        abort(403)