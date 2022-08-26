import csv
import os

import tweepy

from src.constants import RAW_DATA_DIR


def get_tweets(user, api, text=[], pagination_token=None):
    res = api.get_users_tweets(
        user.data.id,
        exclude="retweets",
        max_results=10,
        pagination_token=pagination_token,
    )
    for tweet in res.data:
        text.append([tweet.text])
    try:
        get_tweets(user, api, text, res.meta["next_token"])
        return text
    except Exception:
        return text


def get_output_file(filename, dir=RAW_DATA_DIR):
    output_file = open(f"{dir}/{filename}.csv", "w")
    writer = csv.writer(output_file, lineterminator="\n")
    return output_file, writer


def get_api_client():
    return tweepy.Client(os.getenv("TWITTER_BEARER_TOKEN"))


def write_to_output_file(writer, text, output_file):
    for tweet in text:
        writer.writerow(tweet)
    output_file.close()


def get_all_tweets(username, api):
    print(f"Getting details for {username}...", end="")
    user = api.get_user(username=username)
    print(" done")
    if user.data:
        text = get_tweets(user, api)
        return text
    return None
