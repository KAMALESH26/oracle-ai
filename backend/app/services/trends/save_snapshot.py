from app.database.postgres import db
from app.models.trend_history import (
    TrendHistory
)


def save_snapshot(trends):

    for trend in trends:

        row = TrendHistory(

            keyword=trend["keyword"],

            mentions=trend["mentions"],

            trend_score=trend.get(
                "trend_score",
                float(trend["mentions"])
            )
        )

        db.session.add(row)

    db.session.commit()