#!/usr/bin/python3
""" recursivly getting hot topics """
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """ get recur """
    if word_count is None:
        word_count = {}
    if subreddit is None or type(subreddit) is not str:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    params = {"after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for child in children:
            title = child["data"]["title"].lower()

            for word in word_list:
                word = word.lower()

                if word in title:
                    word_count[word] = word_count.get(word, 0) + 1

        after = data["data"]["after"]
        if after:
            return count_words(subreddit, word_list, word_count, after)
        else:
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print(f"{word}: {count}")
            return
    elif response.status_code == 404:
        return
    else:
        return
