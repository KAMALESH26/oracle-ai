from datetime import datetime

from app.database.postgres import db


class TrendMetric(db.Model):

    __tablename__ = "trend_metrics"

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
        default=0
    )

    trend_score = db.Column(
        db.Float,
        default=0
    )

    source = db.Column(
        db.String(100)
    )

    collected_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )