from collections import Counter

from app.services.topics.topic_mapper import (
    TOPIC_MAP
)

from app.services.trends.trend_score import (
    calculate_trends
)


def calculate_topics():

    trends = calculate_trends()

    topic_counter = Counter()

    for trend in trends:

        keyword = trend["keyword"]

        for topic, keywords in TOPIC_MAP.items():

            if keyword in keywords:

                topic_counter[topic] += (
                    trend["mentions"]
                )

    return topic_counter.most_common()