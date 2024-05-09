#!/usr/bin/python3
"""Module that consumes the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    """ queries the Reddit API and returns a list containing the titles """

    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    r = requests.get(base_url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        r = r.json()
        for post in r.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if r.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
