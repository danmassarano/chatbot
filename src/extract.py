import csv
import os

import tweepy

from src.constants import RAW_DATA_DIR

writer = None
client = None


# TODO: Refactor to return a string, dict, or list
# This should just get data from twitter and return it. Writing out to
# output file should be handled in a seperate method or in the
# chatbot module
# labels: refactor
# assignees: danmassarano
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


# TODO: Refactor all of this
# This should contain seperate methods to create a client, create file,
# get a user, and return a value. Calling get_tweets and closing file
# should be done in a seperate method or in the chatbot module
# labels: refactor
# assignees: danmassarano
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
