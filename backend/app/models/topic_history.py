from datetime import datetime

from app.database.postgres import db


class TopicHistory(db.Model):

    __tablename__ = "topic_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    topic = db.Column(
        db.String(255),
        nullable=False
    )

    mentions = db.Column(
        db.Integer,
        nullable=False
    )

    collected_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )