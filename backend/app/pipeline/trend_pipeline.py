from app.collectors.rss.fetch import (
    fetch_feed,
    RSS_SOURCES
)

from app.collectors.rss.store import (
    save_articles
)

from app.services.trends.trend_score import (
    calculate_trends
)

from app.services.trends.save_snapshot import (
    save_snapshot
)


def run_pipeline():

    print("\n=== ORACLE PIPELINE START ===")

    all_articles = []

    for source in RSS_SOURCES:

        try:

            articles = fetch_feed(source)

            all_articles.extend(
                articles
            )

        except Exception as e:

            print(
                f"{source}: {e}"
            )

    save_articles(
        all_articles
    )

    trends = calculate_trends()

    save_snapshot(
        trends
    )

    print(
        f"Saved {len(trends)} trends"
    )

    print(
        "=== PIPELINE COMPLETE ==="
    )