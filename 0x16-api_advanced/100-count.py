#!/usr/bin/python3
"""
This script counts the number of keywords present in a
subreddit
"""

import json
import requests


def count_words(subreddit, word_list, after=None, count=[]):
    """count all words"""

    if after is None:
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data.get('data').get('children')):
            for word in topic.get('data').get('title').split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data.get('data').get('after')
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)
