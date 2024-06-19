#!/usr/bin/python3
"""
This is my script to retrieve the number of subscribers
in a reddit api
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function returns the number of subscribers in subreddit
    or 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-Reddit-Script"}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
