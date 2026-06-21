from app.collectors.github.fetch import (
    fetch_trending_repositories
)

from app.collectors.github.store import (
    save_repositories
)


repos = fetch_trending_repositories()

save_repositories(repos)