from app.collectors.hackernews.fetch import (
    fetch_hn_posts
)

from app.collectors.hackernews.store import (
    save_posts
)

posts = fetch_hn_posts()

save_posts(posts)