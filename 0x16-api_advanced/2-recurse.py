#!/usr/bin/python3
"""
This script uses recursion to retrieve all subreddits
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    This function is a recursive function that retrieves the
    subreddits's hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-Reddit-Script"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    hot_list.extend([post.get('data').get('title')
                     for post in data.get('children')])
    if data['after'] is not None:
        return recurse(subreddit, hot_list, data['after'])
    else:
        return hot_list
