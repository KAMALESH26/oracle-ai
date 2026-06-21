from datetime import datetime
from app.database.postgres import db


class TrendHistory(db.Model):

    __tablename__ = "trend_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    keyword = db.Column(
        db.String(255),
        nullable=False
    )

    mentions = db.Column(
        db.Integer,
        nullable=False
    )

    trend_score = db.Column(
        db.Float,
        nullable=False
    )

    collected_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )