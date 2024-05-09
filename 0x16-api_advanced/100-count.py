#!/usr/bin/python3
"""ecursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count
of given keywords"""

import requests

def count_words(subreddit, word_list, counts=None):
    """ecursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords"""
    headers = {'User-agent': 'test45'}
    posts_request = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                                 .format(subreddit, after), headers=headers)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts_request.status_code == 200:
        posts_data = posts_request.json()['data']
        next_page = posts_data['after']
        posts_data = posts_data['children']
        for post in posts_data:
            post_title = post['data']['title'].lower()
            for word in post_title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if next_page is not None:
            count_words(subreddit, word_list, found_list, next_page)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
