from app.database.postgres import db
from app.models.trend_metric import TrendMetric


def save_trends(trends):

    for trend in trends:

        metric = TrendMetric(

            keyword=trend["keyword"],

            mentions=trend["mentions"],

            trend_score=trend["trend_score"],

            source="rss"
        )

        db.session.add(metric)

    db.session.commit()