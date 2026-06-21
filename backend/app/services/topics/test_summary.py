from app.services.topics.topic_summary import (
    get_topic_summary
)

for topic in get_topic_summary():

    print(topic)