#!/usr/bin/python3
"""prints the titles of the first"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot
    postsdd listed for a given subreddit. """

    b_url = 'https://www.reddit.com'
    sort = 'top'
    limit = 10
    url = '{}/r/{}/.json?sort={}&limit={}'.format(
        b_url, subreddit, sort, limit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    data = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if data.status_code == 200:
        for post in data.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
