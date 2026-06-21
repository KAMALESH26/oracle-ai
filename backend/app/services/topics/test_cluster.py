from app.services.topics.topic_cluster import (
    assign_topic
)

tests = [

    "openai",

    "anthropic service",

    "battery gamble",

    "hacked leaked"
]

for t in tests:

    print(
        t,
        "->",
        assign_topic(t)
    )