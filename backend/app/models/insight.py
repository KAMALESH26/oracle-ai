# app/models/insight.py

from datetime import datetime

from app.database.postgres import db


class Insight(db.Model):

    __tablename__ = "insights"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    topic_id = db.Column(
        db.Integer,
        db.ForeignKey("topics.id"),
        nullable=False
    )

    report_text = db.Column(
        db.Text,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )