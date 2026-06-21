from app.database.postgres import db


class TopicCluster(db.Model):

    __tablename__ = "topic_clusters"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    topic_name = db.Column(
        db.String(255)
    )

    article_count = db.Column(
        db.Integer
    )