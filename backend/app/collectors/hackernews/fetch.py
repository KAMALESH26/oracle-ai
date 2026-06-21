import requests


def fetch_hn_posts():

    ids = requests.get(

        "https://hacker-news.firebaseio.com/v0/topstories.json"

    ).json()[:50]

    posts = []

    for story_id in ids:

        url = (

            "https://hacker-news.firebaseio.com/v0/item/"

            f"{story_id}.json"
        )

        data = requests.get(url).json()

        posts.append({

            "id": data.get("id"),

            "title": data.get("title"),

            "score": data.get("score"),

            "source": "hackernews"
        })

    return posts