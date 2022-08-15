import csv
import os

from constants import RAW_DATA_DIR

import tweepy

writer = None
client = None


def get_tweets(user, pagination_token=None):
    res = client.get_users_tweets(
        user.data.id,
        exclude="retweets",
        max_results=100,
        pagination_token=pagination_token,
    )
    for tweet in res.data:
        writer.writerow([tweet.text])
    try:
        get_tweets(user, res.meta["next_token"])
    except Exception:
        None


def get_all_tweets(username, output):
    print(f"Getting tweets for {username}...", end="")
    global writer, client

    output_file = open(f"{RAW_DATA_DIR}/{output}.csv", "w")
    writer = csv.writer(output_file, lineterminator="\n")
    client = tweepy.Client(os.getenv("TWITTER_BEARER_TOKEN"))
    user = client.get_user(username=username)

    get_tweets(user)
    print(" done")
    output_file.close()
