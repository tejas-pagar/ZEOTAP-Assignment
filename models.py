from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String, nullable=False)  

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    experience = db.Column(db.Integer, nullable=False)
