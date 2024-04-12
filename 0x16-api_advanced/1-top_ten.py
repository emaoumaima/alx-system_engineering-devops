#!/usr/bin/python3
""" top 10 hot """
import requests


def top_ten(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data["data"]:
            for post in data["data"]["children"]:
                title = post["data"]["title"]
                print(title)
    else:
        print(None)
