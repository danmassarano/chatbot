"""Extract data into a raw source file."""
import csv
import os

import tweepy

from src.constants import RAW_DATA_DIR


def get_tweets(user, api, text=[], pagination_token=None):
    """
    Recursively get all tweets for a given user ID.

    Args:
        user (str): User ID for a given Twitter user
        api (Client): Twitter APIv2 client
        text (list), optional: Text list of all tweets
        pagination_token (str), optional: Token to point to next page

    Returns
        text (list): Text list of all tweets

    """
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
    """
    Create a connection to write to a file.

    Args:
        filename (str): Name of the file to write to
        dir (str): Name of directory to write to

    Returns
        output_file (TextIOWrapper): Connection of file to write to
        writer (csv.writer): CSV writer

    """
    output_file = open(f"{dir}/{filename}.csv", "w")
    writer = csv.writer(output_file, lineterminator="\n")
    return output_file, writer


def get_api_client():
    """
    Create a connection to the Twitter API.

    Args:
        None

    Returns
        API (tweepy.Client): API client connection

    """
    return tweepy.Client(os.getenv("TWITTER_BEARER_TOKEN"))


def write_to_output_file(writer, text, output_file):
    """
    Write all text into a CSV file and closes the file.

    Args:
        writer (csv.writer): CSV writer
        text (list): Text list of all tweets
        output_file (TextIOWrapper): Connection of file to write to

    Returns
        None

    """
    for tweet in text:
        writer.writerow(tweet)
    output_file.close()


def get_all_tweets(username, api):
    """
    Find the ID of a given user and get all of their tweets.

    Args:
        username (str): Username for a given Twitter user
        api (Client): Twitter APIv2 client

    Returns
        text (list): Text list of all tweets

    """
    print(f"Getting details for {username}...", end="")
    user = api.get_user(username=username)
    print(" done")
    if user.data:
        text = get_tweets(user, api)
        return text
    return None
