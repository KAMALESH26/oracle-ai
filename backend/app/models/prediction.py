# app/models/prediction.py

from datetime import datetime

from app.database.postgres import db


class Prediction(db.Model):

    __tablename__ = "predictions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    topic_id = db.Column(
        db.Integer,
        db.ForeignKey("topics.id"),
        nullable=False
    )

    predicted_mentions = db.Column(
        db.Integer
    )

    predicted_growth = db.Column(
        db.Float
    )

    predicted_score = db.Column(
        db.Float
    )

    confidence = db.Column(
        db.Float
    )

    prediction_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )