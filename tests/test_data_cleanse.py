"""test_data_cleanse runs unit tests on the data_cleanse module."""
import os
import sys
import unittest
from os.path import exists

from test_constants import CLEANED_DATA_DIR
from test_constants import EXPECTED_DATA_DIR
from test_constants import RAW_DATA_DIR

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "chatbot")
sys.path.append(SOURCE_PATH)

from chatbot.data_cleanse import clean_data_unstructured  # noqa: E402
from chatbot.data_cleanse import clean_input_files  # noqa: E402
from chatbot.data_cleanse import clean_line  # noqa: E402


class TestDataCleanse(unittest.TestCase):
    """
    Runs unit tests on the data_cleanse module.

    Methods
    -------
    test_clean_line():
        Test that cleaning a single line works as expected.
    test_clean_line_links():
        Test that links are removed.
    test_clean_line_username():
        Test that usernames are removed.
    test_clean_line_usernames():
        Test that multiple usernames are removed.
    test_clean_line_numbers():
        Test that numbers are removed.
    test_clean_whitespace():
        Test that extra whitespace is removed.
    test_clean_csv_file():
        Tests that csv file is processed correctly.
    test_clean_text_file():
        Tests that text file is processed correctly.
    test_clean_input_files():
        Tests that all files are processed.

    """

    def test_clean_line(self):
        """Test that cleaning a single line works as expected."""
        line = "@uname1 thoughts, chaps? https://t.co/AVra5sdv"
        expected = "thoughts, chaps?"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_links(self):
        """Test that links are removed."""
        line = "Here https://t.co/AVra5sdv"
        expected = "Here"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_username(self):
        """Test that usernames are removed."""
        line = "@uname1 thoughts"
        expected = "thoughts"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_usernames(self):
        """Test that multiple usernames are removed."""
        line = "@uname2 @uname2 @uname3 I think"
        expected = "I think"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_numbers(self):
        """Test that numbers are removed."""
        line = "1234"
        expected = ""
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_whitespace(self):
        """Test that extra whitespace is removed."""
        line = "    "
        expected = ""
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_csv_file(self):
        """Tests that csv file is processed correctly."""
        filename = "test_csv.csv"

        try:
            clean_data_unstructured(filename, RAW_DATA_DIR, CLEANED_DATA_DIR)

            expected_file = open(f"{EXPECTED_DATA_DIR}/{filename}", "r")
            expected = expected_file.read()
            expected_file.close()

            result_file = open(f"{CLEANED_DATA_DIR}/{filename}", "r")
            result = result_file.read()
            result_file.close()

            self.assertEqual(result, expected)

        finally:
            if exists(f"{CLEANED_DATA_DIR}/{filename}"):
                os.remove(f"{CLEANED_DATA_DIR}/{filename}")
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)

    def test_clean_text_file(self):
        """Tests that text file is processed correctly."""
        filename = "test_txt.txt"

        try:
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)

            clean_data_unstructured(filename, RAW_DATA_DIR, CLEANED_DATA_DIR)

            expected_file = open(f"{EXPECTED_DATA_DIR}/{filename}", "r")
            expected = expected_file.read()
            expected_file.close()

            result_file = open(f"{CLEANED_DATA_DIR}/{filename}", "r")
            result = result_file.read()
            result_file.close()

            self.assertEqual(result, expected)

        finally:
            if exists(f"{CLEANED_DATA_DIR}/{filename}"):
                os.remove(f"{CLEANED_DATA_DIR}/{filename}")
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)

    def test_clean_input_files(self):
        """Tests that all files are processed."""
        expected_txt = f"{CLEANED_DATA_DIR}/test_txt.txt"
        expected_csv = f"{CLEANED_DATA_DIR}/test_csv.csv"

        try:
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)

            clean_input_files(RAW_DATA_DIR, CLEANED_DATA_DIR)

            self.assertTrue(exists(expected_txt))
            self.assertTrue(exists(expected_csv))

        finally:
            if exists(expected_txt):
                os.remove(expected_txt)
            if exists(expected_csv):
                os.remove(expected_csv)
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)
