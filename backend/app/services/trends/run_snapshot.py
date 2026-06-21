from app.main import app

from app.services.trends.aggregate_keywords import (
    get_top_trends
)

from app.services.trends.save_snapshot import (
    save_snapshot
)


def run_snapshot():

    with app.app_context():

        trends = get_top_trends()

        save_snapshot(
            trends
        )

        print(
            f"Saved {len(trends)} trends"
        )