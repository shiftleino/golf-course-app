from src.app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from src.app import app

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
