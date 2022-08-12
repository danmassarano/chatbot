import csv
import os

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
        print(tweet.text)
    try:
        get_tweets(res.meta["next_token"])
    except:
        print("\nEnd of tweets\n")


def get_all_tweets(username, output):
    global writer, client

    output_file = open("input/" + output + ".csv", "w")
    writer = csv.writer(output_file, lineterminator="\n")
    client = tweepy.Client(os.getenv("TWITTER_BEARER_TOKEN"))
    user = client.get_user(username=username)

    get_tweets(user)

    output_file.close()


get_all_tweets("edthewlis", "twitter_dump")
# get_all_tweets("elonmusk", "twitter_dump")
