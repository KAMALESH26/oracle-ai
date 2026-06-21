# app/models/keyword.py

from app.database.postgres import db


class Keyword(db.Model):

    __tablename__ = "keywords"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    topic_id = db.Column(
        db.Integer,
        db.ForeignKey("topics.id"),
        nullable=False
    )

    keyword = db.Column(
        db.String(255),
        nullable=False
    )

    frequency = db.Column(
        db.Integer,
        default=0
    )