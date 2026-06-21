from app.services.trends.run_snapshot import (
    run_snapshot)
from app.services.topics.topic_summary import (
    get_topic_summary
)

from app.services.topics.save_topic_snapshot import (
    save_topic_snapshot
)



def collect_trends():

    print(
        "Running trend collection..."
    )

    run_snapshot()

    print(
        "Collection complete"
    )

    topics = get_topic_summary()

    save_topic_snapshot(
        topics
    )