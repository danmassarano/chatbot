import os
import unittest
from collections import namedtuple
from os.path import exists
from unittest import mock

import tweepy
from test_constants import CLEANED_DATA_DIR

from src.extract import get_all_tweets


class TestExtract(unittest.TestCase):
    def test_second(mocker):
        """
        Test that tweets are fetched for a given user
        """

        filename = "test_csv"

        try:
            with mock.patch("src.extract.tweepy.Client") as mock_client:
                with mock.patch("tweepy.client.Client.get_user") as mock_user:
                    with mock.patch(
                        "tweepy.client.Client.get_users_tweets"
                    ) as mock_tweets:
                        mock_client.return_value = tweepy.client.Client

                        Data = namedtuple("data", ["id", "name", "username"])
                        User = namedtuple("user", "data")
                        user = User(Data(28785486, "ABC News", "ABC"))

                        Data = namedtuple("data", "text")
                        Tweet = namedtuple("tweet", ["data"])
                        res = Tweet([Data("test value"), Data("another")])

                        mock_user.return_value = user
                        mock_tweets.return_value = res
                        get_all_tweets("123", filename, CLEANED_DATA_DIR)

                        mock_user.assert_called_once()
                        mock_tweets.assert_called_once()
                        mocker.assertTrue(
                            exists(f"{CLEANED_DATA_DIR}/{filename}.csv")
                        )

        finally:
            if exists(f"{CLEANED_DATA_DIR}/{filename}.csv"):
                os.remove(f"{CLEANED_DATA_DIR}/{filename}.csv")
