import os
import unittest
from collections import namedtuple
from os.path import exists
from unittest import mock

import tweepy
from test_constants import CLEANED_DATA_DIR

from src.extract import get_all_tweets
from src.extract import get_api_client
from src.extract import get_output_file


class TestExtract(unittest.TestCase):
    def test_get_api_client(mocker):
        """
        Test that api client is called correctly
        """
        with mock.patch("src.extract.tweepy.Client") as mock_client:
            mock_client.return_value = tweepy.client.Client
            result = get_api_client()
            mock_client.assert_called_once()
            mocker.assertIsNotNone(result)

    def test_get_output_file(self):
        """
        Test that an output file and writer are generated
        """

        filename = "test_csv"

        try:
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)
            expected_filename = f"{CLEANED_DATA_DIR}/{filename}.csv"
            output_file, writer = get_output_file(
                filename, dir=CLEANED_DATA_DIR
            )
            self.assertIsNotNone(output_file)
            self.assertIsNotNone(writer)
            self.assertEqual(expected_filename, output_file.name)
            output_file.close()

        finally:
            if exists(f"{CLEANED_DATA_DIR}/{filename}.csv"):
                os.remove(f"{CLEANED_DATA_DIR}/{filename}.csv")
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)

    def test_get_all_tweets(mocker):
        """
        Test that tweets are fetched for a given user
        """

        filename = "test_csv"

        try:
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)

            with mock.patch("src.extract.tweepy.Client") as mock_client:
                with mock.patch("tweepy.client.Client.get_user") as mock_user:
                    with mock.patch(
                        "tweepy.client.Client.get_users_tweets"
                    ) as mock_tweets:
                        output_file, writer = get_output_file(
                            filename, dir=CLEANED_DATA_DIR
                        )

                        mock_client.return_value = tweepy.client.Client
                        api = get_api_client()

                        Data = namedtuple("data", ["id", "name", "username"])
                        User = namedtuple("user", "data")
                        user = User(Data(28785486, "ABC News", "ABC"))

                        Data = namedtuple("data", "text")
                        Tweet = namedtuple("tweet", ["data"])
                        res = Tweet([Data("test value"), Data("another")])

                        mock_user.return_value = user
                        mock_tweets.return_value = res
                        get_all_tweets("123", api, writer)

                        mock_user.assert_called_once()
                        mock_tweets.assert_called_once()
                        mocker.assertTrue(
                            exists(f"{CLEANED_DATA_DIR}/{filename}.csv")
                        )
                        output_file.close()

        finally:
            if exists(f"{CLEANED_DATA_DIR}/{filename}.csv"):
                os.remove(f"{CLEANED_DATA_DIR}/{filename}.csv")
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)
