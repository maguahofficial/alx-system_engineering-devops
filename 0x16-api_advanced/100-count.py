#!/usr/bin/python3
"""
The Function that queries the Reddit API then prints
the top ten hot posts of a subreddit
"""
import re
import requests


def add_title(dictionary, hot_posts):
    """This function Adds item into a list """
    if len(hot_posts) == 0:
        return

    titlex = hot_posts[0]['data']['title'].split()
    for word in titlex:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ This function queries the Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dicx = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dicx['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list, dictionary=None):
    """ The Init function """
    if dictionary is None:
        dictionary = {}

    for wordx in word_list:
        wordx = word.lower()
        if wordx not in dictionary:
            dictionary[wordx] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for item in sorted_items:
        if item[1] > 0:
            print("{}: {}".format(item[0], item[1]))
