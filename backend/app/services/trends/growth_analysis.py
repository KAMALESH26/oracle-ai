from collections import defaultdict

from app.models.trend_history import (
    TrendHistory
)


def calculate_growth():

    keyword_data = defaultdict(list)

    rows = TrendHistory.query.order_by(
        TrendHistory.collected_at.asc()
    ).all()

    for row in rows:

        keyword_data[
            row.keyword
        ].append(row.mentions)

    growth_results = []

    for keyword, mentions in keyword_data.items():

        if len(mentions) < 2:
            continue

        previous = mentions[-2]
        current = mentions[-1]

        if previous == 0:
            continue

        growth = (
            (current - previous)
            / previous
        ) * 100

        growth_results.append({

            "keyword": keyword,

            "previous": previous,

            "current": current,

            "growth": round(
                growth,
                2
            )
        })

    growth_results.sort(

        key=lambda x: x["growth"],

        reverse=True
    )

    return growth_results