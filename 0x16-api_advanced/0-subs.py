#!/usr/bin/python3
""" function returns the number of subscribers """

import requests as req


def number_of_subscribers(subreddit):
    """ this function will return the number of subs of a given subreddit """

    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    responses = req.get(url, headers=headers, allow_redirects=False)

    if responses.status_code == 200:
        return (responses.json().get("data").get("subscribers"))
    return (0)
