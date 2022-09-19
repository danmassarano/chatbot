"""test_data_cleanse runs unit tests on the data_cleanse module."""
import os
import sys
import unittest
from os.path import exists

from test_constants import CLEANED_DATA_DIR
from test_constants import EXPECTED_DATA_DIR
from test_constants import RAW_DATA_DIR
from test_constants import STAGING_DATA_DIR
from test_constants import UNSTAGED_FILE

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "chatbot")
sys.path.append(SOURCE_PATH)

from chatbot.data_cleanse import clean_data_unstructured  # noqa: E402
from chatbot.data_cleanse import clean_input_files  # noqa: E402
from chatbot.data_cleanse import clean_line  # noqa: E402
from chatbot.data_cleanse import load_text_file  # noqa: E402
from chatbot.data_cleanse import load_csv_file  # noqa: E402
from chatbot.data_cleanse import load_json_file  # noqa: E402
from chatbot.data_cleanse import load_input_files  # noqa: E402
from chatbot.data_cleanse import unstage_cleansed_files  # noqa: E402


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
    test_load_text_file():
        Test that text file loads into a string.
    test_load_csv_file():
        Test that csv file loads into a string.
    test_load_json_file():
        Test that JSON file loads into a string.
    test_load_input_files():
        Test that files are loaded into a string.
    test_unstage_cleansed_files():
        Tests that all files are unstaged into a single file.

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
            clean_data_unstructured(filename, RAW_DATA_DIR, STAGING_DATA_DIR)

            expected_file = open(f"{EXPECTED_DATA_DIR}/{filename}", "r")
            expected = expected_file.read()
            expected_file.close()

            result_file = open(f"{STAGING_DATA_DIR}/{filename}", "r")
            result = result_file.read()
            result_file.close()

            self.assertEqual(result, expected)

        finally:
            if exists(f"{STAGING_DATA_DIR}/{filename}"):
                os.remove(f"{STAGING_DATA_DIR}/{filename}")
            if os.path.exists(STAGING_DATA_DIR):
                os.rmdir(STAGING_DATA_DIR)

    def test_clean_text_file(self):
        """Tests that text file is processed correctly."""
        filename = "test_txt.txt"

        try:
            if not os.path.exists(STAGING_DATA_DIR):
                os.makedirs(STAGING_DATA_DIR)

            clean_data_unstructured(filename, RAW_DATA_DIR, STAGING_DATA_DIR)

            expected_file = open(f"{EXPECTED_DATA_DIR}/{filename}", "r")
            expected = expected_file.read()
            expected_file.close()

            result_file = open(f"{STAGING_DATA_DIR}/{filename}", "r")
            result = result_file.read()
            result_file.close()

            self.assertEqual(result, expected)

        finally:
            if exists(f"{STAGING_DATA_DIR}/{filename}"):
                os.remove(f"{STAGING_DATA_DIR}/{filename}")
            if os.path.exists(STAGING_DATA_DIR):
                os.rmdir(STAGING_DATA_DIR)

    def test_clean_input_files(self):
        """Tests that all files are processed."""
        expected_txt = f"{STAGING_DATA_DIR}/test_txt.txt"
        expected_csv = f"{STAGING_DATA_DIR}/test_csv.csv"

        try:
            if not os.path.exists(STAGING_DATA_DIR):
                os.makedirs(STAGING_DATA_DIR)

            clean_input_files(RAW_DATA_DIR, STAGING_DATA_DIR)

            self.assertTrue(exists(expected_txt))
            self.assertTrue(exists(expected_csv))

        finally:
            if exists(expected_txt):
                os.remove(expected_txt)
            if exists(expected_csv):
                os.remove(expected_csv)
            if os.path.exists(STAGING_DATA_DIR):
                os.rmdir(STAGING_DATA_DIR)

    def test_load_text_file(self):
        """Test that text file loads into a string."""
        filename = "test_txt.txt"
        result = load_text_file(filename, EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_load_csv_file(self):
        """Test that csv file loads into a string."""
        filename = "test_csv.csv"
        result = load_csv_file(filename, EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_load_json_file(self):
        """Test that JSON file loads into a string."""
        filename = "test_json.json"
        result = load_json_file(filename, "text", EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_load_input_files(self):
        """Test that files are loaded into a string."""
        result = load_input_files(EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_unstage_cleansed_files(self):
        """Tests that all files are unstaged into a single file."""
        source_txt = f"{STAGING_DATA_DIR}/test_txt.txt"
        source_csv = f"{STAGING_DATA_DIR}/test_csv.csv"
        expected_txt = f"{CLEANED_DATA_DIR}/{UNSTAGED_FILE}"

        try:
            if not os.path.exists(STAGING_DATA_DIR):
                os.makedirs(STAGING_DATA_DIR)
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)

            clean_input_files(RAW_DATA_DIR, STAGING_DATA_DIR)
            unstage_cleansed_files(
                STAGING_DATA_DIR, CLEANED_DATA_DIR, UNSTAGED_FILE
            )

            self.assertTrue(exists(expected_txt))

        finally:
            if exists(source_txt):
                os.remove(source_txt)
            if exists(source_csv):
                os.remove(source_csv)
            if exists(expected_txt):
                os.remove(expected_txt)
            if os.path.exists(STAGING_DATA_DIR):
                os.rmdir(STAGING_DATA_DIR)
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)
