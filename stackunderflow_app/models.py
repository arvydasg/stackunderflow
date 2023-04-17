from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
import pytz

db = SQLAlchemy()

tz = pytz.timezone("Europe/Vilnius")
now = datetime.now(tz)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(20), default="default.jpg")
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(tz))


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    content = db.Column(db.String(5000))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = db.relationship(
        "Users", backref="questions"
    )  # allows to access the name of the author instead of id
    created_at = db.Column(db.DateTime, default=datetime.now(tz))
    modified_at = db.Column(
        db.DateTime, default=None, onupdate=datetime.now(tz)
    )  # onupdate method allows to specify an SQL expression that will
    # be executed when the row is updated


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(5000))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = db.relationship("Users")
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    question = db.relationship("Question", backref=db.backref("answers", lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.now(tz))
    modified_at = db.Column(db.DateTime)

    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)

    # only update the "modified_at" field when content field is updated, not when liked/disliked
    @validates("content")
    def update_modified_at(self, key, content):
        if self.content != content:
            self.modified_at = datetime.now(tz)
        return content


class Action(db.Model):
    __tablename__ = "actions"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey("answer.id"), primary_key=True)
    action = db.Column(db.String(10))
