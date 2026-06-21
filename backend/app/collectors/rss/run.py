from app.collectors.rss.fetch import fetch_feed
from app.collectors.rss.store import save_articles


articles = fetch_feed("techcrunch")

save_articles(articles)