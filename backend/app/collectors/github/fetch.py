import requests

from app.config.settings import Config


def fetch_trending_repositories():

    headers = {

        "Authorization":
        f"Bearer {Config.GITHUB_TOKEN}",

        "Accept":
        "application/vnd.github+json"
    }

    url = (
        "https://api.github.com/"
        "search/repositories"
    )

    params = {

        "q": "stars:>1000",

        "sort": "stars",

        "order": "desc",

        "per_page": 50
    }

    response = requests.get(

        url,

        headers=headers,

        params=params
    )

    data = response.json()

    repositories = []

    for repo in data["items"]:

        repositories.append({

            "repository":
            repo["full_name"],

            "description":
            repo["description"],

            "language":
            repo["language"],

            "stars":
            repo["stargazers_count"],

            "url":
            repo["html_url"],

            "source":
            "github"
        })

    return repositories