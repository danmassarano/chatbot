"""test_markov_chain runs unit tests on the markov_chain module."""
import os
import sys
import unittest

from test_constants import EXPECTED_DATA_DIR

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, "chatbot")
sys.path.append(SOURCE_PATH)

from chatbot.markov_chain import load_csv_file  # noqa: E402
from chatbot.markov_chain import load_input_files  # noqa: E402
from chatbot.markov_chain import load_json_file  # noqa: E402
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
    test_load_csv_file():
        Test that csv file loads into a string.
    test_load_json_file():
        Test that JSON file loads into a string.
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

    def test_train_text_model(self):
        """Test that files are loaded into a trained text model."""
        training_data = load_input_files(EXPECTED_DATA_DIR)
        result = train_text_model(training_data)
        self.assertIsNotNone(result)

    def test_output_sentence(self):
        """Test that a regular sentence is generated correctly."""
        training_data = load_input_files(EXPECTED_DATA_DIR)
        text_model = train_text_model(training_data)
        for _ in range(5):
            result = output_sentence(text_model)
            self.assertIsNotNone(result)

    def test_output_short_sentence(self):
        """Test that a regular sentence is generated correctly."""
        training_data = load_input_files(EXPECTED_DATA_DIR)
        text_model = train_text_model(training_data)
        for _ in range(5):
            result = output_short_sentence(text_model, 280)
            self.assertIsNotNone(result)
