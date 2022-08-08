import csv
import os

import tweepy


def get_tweets(pagination_token=None):
    res = client.get_users_tweets(
        ed.data.id,
        exclude="retweets",
        max_results=100,
        pagination_token=pagination_token,
    )
    print("writing out tweets...")
    for tweet in res.data:
        writer.writerow([tweet.text])
    if res.meta["next_token"]:
        get_tweets(res.meta["next_token"])


f = open("source/edthewlis_twitter_dump.csv", "w")
writer = csv.writer(f, lineterminator="\n")

client = tweepy.Client(os.getenv("TWITTER_BEARER_TOKEN"))

ed = client.get_user(username="edthewlis")
print(ed)

get_tweets()

f.close()
