# app/models/topic.py

from datetime import datetime

from app.database.postgres import db


class Topic(db.Model):

    __tablename__ = "topics"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )

    category = db.Column(
        db.String(100)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )