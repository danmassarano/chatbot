import csv
import os

import tweepy

from src.constants import RAW_DATA_DIR

writer = None
client = None


def get_tweets(user, pagination_token=None):
    res = client.get_users_tweets(
        user.data.id,
        exclude="retweets",
        max_results=10,
        pagination_token=pagination_token,
    )
    print(res)
    for tweet in res.data:
        writer.writerow([tweet.text])
    try:
        get_tweets(user, res.meta["next_token"])
    except Exception:
        None


def get_all_tweets(username, output, dir=RAW_DATA_DIR):
    print(f"Getting tweets for {username}...", end="")
    global writer, client

    output_file = open(f"{dir}/{output}.csv", "w")
    writer = csv.writer(output_file, lineterminator="\n")
    client = tweepy.Client(os.getenv("TWITTER_BEARER_TOKEN"))
    user = client.get_user(username=username)
    print(user)
    print(type(user))
    if user.data:
        get_tweets(user)
    print(" done")
    output_file.close()
