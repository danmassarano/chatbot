"""test_extract runs unit tests on the extract module."""
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
from src.extract import write_to_output_file


class TestExtract(unittest.TestCase):
    """
    Runs unit tests on the extract module.

    Methods
    -------
    test_get_api_client(mocker):
        Test that api client is called correctly.
    test_get_output_file():
        Test that an output file and writer are generated.
    test_write_to_output_file():
        Test that text is written to an output file.
    test_get_all_tweets(mocker):
        Test that tweets are fetched for a given user.

    """

    def test_get_api_client(mocker):
        """Test that api client is called correctly."""
        with mock.patch("src.extract.tweepy.Client") as mock_client:
            mock_client.return_value = tweepy.client.Client
            result = get_api_client()
            mock_client.assert_called_once()
            mocker.assertIsNotNone(result)

    def test_get_output_file(self):
        """Test that an output file and writer are generated."""
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

    def test_write_to_output_file(self):
        """Test that text is written to an output file."""
        filename = "test_csv"

        try:
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)
            output_file, writer = get_output_file(
                filename, dir=CLEANED_DATA_DIR
            )
            text = ["test1", "test2"]
            write_to_output_file(writer, text, output_file)

            self.assertIsNotNone(output_file)
            self.assertIsNotNone(writer)
            output_file.close()

        finally:
            if exists(f"{CLEANED_DATA_DIR}/{filename}.csv"):
                os.remove(f"{CLEANED_DATA_DIR}/{filename}.csv")
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)

    def test_get_all_tweets(mocker):
        """Test that tweets are fetched for a given user."""
        with mock.patch("src.extract.tweepy.Client") as mock_client:
            with mock.patch("tweepy.client.Client.get_user") as mock_user:
                with mock.patch(
                    "tweepy.client.Client.get_users_tweets"
                ) as mock_tweets:
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
                    result = get_all_tweets("123", api)

                    mock_user.assert_called_once()
                    mock_tweets.assert_called_once()
                    mocker.assertEqual(result, ([[t.text] for t in res.data]))
