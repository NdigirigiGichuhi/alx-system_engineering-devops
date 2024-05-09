#!/usr/bin/python3
"""ecursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count
of given keywords"""

import requests

def count_words(subreddit, word_list, counts=None):
    """ecursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords"""
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyBot/0.0.1'}  # Setting a custom User-Agent to avoid errors
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    if word.lower() in counts:
                        counts[word.lower()] += 1
                    else:
                        counts[word.lower()] = 1
        if data['data']['after'] is not None:
            count_words(subreddit, word_list, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print(None)

