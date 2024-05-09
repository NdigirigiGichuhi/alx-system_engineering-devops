#!/usr/bin/python3
'''Number of subscribers module'''

import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers (not
    active users, total subscribers) for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
