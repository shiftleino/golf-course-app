from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from database.db import db

def signup(username, password):
    if len(username) < 3 or len(password) < 3:
        return False
    hash_value = generate_password_hash(password)
    sql = "INSERT INTO Users (username, password, role) VALUES (:username, :password, 0)"
    db.session.execute(sql, {"username": username, "password": hash_value})
    db.session.commit()
    return True

def login(username, password):
    sql = "SELECT id, password FROM Users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            return True
        return False
    

