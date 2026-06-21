from app.main import app

from app.services.trends.trend_score import (
    calculate_trends
)

from app.services.trends.save_trends import (
    save_trends
)


with app.app_context():

    trends = calculate_trends()

    save_trends(trends)

    print(
        f"Saved {len(trends)} trends"
    )