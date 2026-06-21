TOPIC_MAP = {

    "Generative AI": [

        "openai",
        "anthropic",
        "claude",
        "gemini",
        "chatgpt",
        "llm"
    ],

    "Cybersecurity": [

        "breach",
        "ransom",
        "hacked",
        "security",
        "threat"
    ],

    "Electric Vehicles": [

        "ev",
        "battery",
        "tesla"
    ],

    "SaaS Platforms": [

        "notion",
        "service",
        "uptime"
    ]
}


def assign_topic(keyword):

    keyword = keyword.lower()

    for topic, words in TOPIC_MAP.items():

        for word in words:

            if word in keyword:

                return topic

    return "Other"