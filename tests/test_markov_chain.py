"""test_markov_chain runs unit tests on the markov_chain module."""
import os
import sys
import unittest
from os.path import exists

from test_constants import CLEANED_DATA_DIR
from test_constants import EXPECTED_DATA_DIR
from test_constants import UNSTAGED_FILE

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "chatbot")
sys.path.append(SOURCE_PATH)

from chatbot.data_cleanse import unstage_cleansed_files  # noqa: E402
from chatbot.markov_chain import load_input_files  # noqa: E402
from chatbot.markov_chain import load_text_file  # noqa: E402
from chatbot.markov_chain import output_sentence  # noqa: E402
from chatbot.markov_chain import output_short_sentence  # noqa: E402
from chatbot.markov_chain import train_text_model  # noqa: E402


class TestMarkovChain(unittest.TestCase):
    """
    Runs unit tests on the markov_chain module.

    Methods
    -------
    test_load_text_file():
        Test that text file loads into a string.
    test_load_input_files():
        Test that files are loaded into a string.
    test_train_text_model():
        Test that files are loaded into a trained text model.
    test_output_sentence():
        Test that a regular sentence is generated correctly.
    test_output_short_sentence():
        Test that a regular sentence is generated correctly.

    """

    def test_load_text_file(self):
        """Test that text file loads into a string."""
        filename = "test_txt.txt"
        result = load_text_file(filename, EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_load_input_files(self):
        """Test that files are loaded into a string."""
        filename = "test_txt.txt"
        result = load_input_files(EXPECTED_DATA_DIR, filename)
        self.assertIsNotNone(result)

    def test_train_text_model(self):
        """Test that files are loaded into a trained text model."""
        filename = "test_txt.txt"
        training_data = load_input_files(EXPECTED_DATA_DIR, filename)
        result = train_text_model(training_data)
        self.assertIsNotNone(result)

    def test_output_sentence(self):
        """Test that a regular sentence is generated correctly."""
        expected_txt = f"{CLEANED_DATA_DIR}/{UNSTAGED_FILE}"
        try:
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)
            unstage_cleansed_files(
                EXPECTED_DATA_DIR, CLEANED_DATA_DIR, UNSTAGED_FILE
            )
            training_data = load_input_files(CLEANED_DATA_DIR, UNSTAGED_FILE)
            text_model = train_text_model(training_data)
            for _ in range(5):
                result = output_sentence(text_model)
                self.assertIsNotNone(result)
        finally:
            if exists(expected_txt):
                os.remove(expected_txt)
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)

    def test_output_short_sentence(self):
        """Test that a regular sentence is generated correctly."""
        expected_txt = f"{CLEANED_DATA_DIR}/{UNSTAGED_FILE}"
        try:
            if not os.path.exists(CLEANED_DATA_DIR):
                os.makedirs(CLEANED_DATA_DIR)
            unstage_cleansed_files(
                EXPECTED_DATA_DIR, CLEANED_DATA_DIR, UNSTAGED_FILE
            )
            training_data = load_input_files(CLEANED_DATA_DIR, UNSTAGED_FILE)
            text_model = train_text_model(training_data)
            for _ in range(5):
                result = output_short_sentence(text_model, 280)
                self.assertIsNotNone(result)
        finally:
            if exists(expected_txt):
                os.remove(expected_txt)
            if os.path.exists(CLEANED_DATA_DIR):
                os.rmdir(CLEANED_DATA_DIR)
