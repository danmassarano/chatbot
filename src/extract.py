import csv
import os

import tweepy

from src.constants import RAW_DATA_DIR


# TODO: Refactor to return a string, dict, or list
# This should just get data from twitter and return it. Writing out to
# output file should be handled in a seperate method or in the
# chatbot module
# labels: refactor
# assignees: danmassarano
def get_tweets(user, api, writer, pagination_token=None):
    res = api.get_users_tweets(
        user.data.id,
        exclude="retweets",
        max_results=10,
        pagination_token=pagination_token,
    )
    for tweet in res.data:
        writer.writerow([tweet.text])
    try:
        get_tweets(user, api, writer, res.meta["next_token"])
    except Exception:
        None


def get_output_file(filename, dir=RAW_DATA_DIR):
    output_file = open(f"{dir}/{filename}.csv", "w")
    writer = csv.writer(output_file, lineterminator="\n")
    print(output_file.name)
    return output_file, writer


def get_api_client():
    return tweepy.Client(os.getenv("TWITTER_BEARER_TOKEN"))


def get_all_tweets(username, api, writer):
    print(f"Getting details for {username}...", end="")
    user = api.get_user(username=username)
    print(" done")
    if user.data:
        get_tweets(user, api, writer)
