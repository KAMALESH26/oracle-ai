from collections import Counter

from app.services.trends.aggregate_keywords import (
    get_top_trends
)

from app.services.topics.topic_cluster import (
    assign_topic
)


def get_topic_summary():

    trends = get_top_trends()

    counter = Counter()

    for trend in trends:

        topic = assign_topic(
            trend["keyword"]
        )

        counter[topic] += (
            trend["mentions"]
        )

    return [

        {

            "topic": topic,

            "mentions": count

        }

        for topic, count
        in counter.most_common()
    ]