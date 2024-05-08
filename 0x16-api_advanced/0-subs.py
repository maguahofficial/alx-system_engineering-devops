#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Function Returns the number of subscribers of a given subreddit."""
    try:
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'MyBot/1.0'}  # Set a custom User-Agent
        responses = requests.get(url, headers=headers, allow_redirects=False)

        if responses.status_code == 200:
            data = responses.json().get("data", {})
            subscribers = data.get("subscribers", 0)
            return subscribers
        else:
            print(f"Error: Received status code {response.status_code} for subreddit '{subreddit}'")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

subreddit = "python"
print(f"Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")

