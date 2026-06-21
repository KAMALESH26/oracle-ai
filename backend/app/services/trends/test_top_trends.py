from app.services.trends.aggregate_keywords import (
    get_top_trends
)

trends = get_top_trends()

for trend in trends[:5]:

    print(trend)