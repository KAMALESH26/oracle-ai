import feedparser


RSS_SOURCES = {
    "techcrunch":
    "https://techcrunch.com/feed/",

    "ars":
    "https://feeds.arstechnica.com/arstechnica/index",

    "wired":
    "https://www.wired.com/feed/rss"
}


def fetch_feed(feed_name):

    url = RSS_SOURCES[feed_name]

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:20]:

        articles.append({
            "title": entry.get("title"),
            "link": entry.get("link"),
            "published": entry.get("published")
        })

    return articles