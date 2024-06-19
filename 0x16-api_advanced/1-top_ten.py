#!/usr/bin/python3
"""
This script contains a function that gets the top 10
hot posts for a subreddit
"""

import requests


def top_ten(subreddit):
    """
    This function retrieves the top 10 hottest
    posts in a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My-Reddit-Script"}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json().get('data').get('children')
    for post in data:
        print(post.get('data').get('title'))
