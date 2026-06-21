from app.collectors.rss.fetch import (
    fetch_feed,
    RSS_SOURCES
)

from app.collectors.rss.store import (
    save_articles
)

for source in RSS_SOURCES:

    print(f"\nCollecting {source}")

    articles = fetch_feed(source)

    save_articles(articles)