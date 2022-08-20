import unittest

from test_constants import EXPECTED_DATA_DIR

from src.markov_chain import load_csv_file
from src.markov_chain import load_input_files
from src.markov_chain import load_json_file
from src.markov_chain import load_text_file
from src.markov_chain import output_sentence
from src.markov_chain import output_short_sentence
from src.markov_chain import train_text_model


class TestMarkovChain(unittest.TestCase):
    def test_load_text_file(self):
        """
        Test that text file loads into a string
        """
        filename = "test_txt.txt"
        result = load_text_file(filename, EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_load_csv_file(self):
        """
        Test that csv file loads into a string
        """
        filename = "test_csv.csv"
        result = load_csv_file(filename, EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_load_json_file(self):
        """
        Test that JSON file loads into a string
        """
        filename = "test_json.json"
        result = load_json_file(filename, "text", EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_load_input_files(self):
        """
        Test that files are loaded into a string
        """
        result = load_input_files(EXPECTED_DATA_DIR)
        self.assertIsNotNone(result)

    def test_train_text_model(self):
        """
        Test that files are loaded into a trained text model
        """
        training_data = load_input_files(EXPECTED_DATA_DIR)
        result = train_text_model(training_data)
        self.assertIsNotNone(result)

    def test_output_sentence(self):
        """
        Test that a regular sentence is generated correctly
        """
        training_data = load_input_files(EXPECTED_DATA_DIR)
        text_model = train_text_model(training_data)
        for _ in range(5):
            result = output_sentence(text_model)
            self.assertIsNotNone(result)

    def test_output_short_sentence(self):
        """
        Test that a regular sentence is generated correctly
        """
        training_data = load_input_files(EXPECTED_DATA_DIR)
        text_model = train_text_model(training_data)
        for _ in range(5):
            result = output_short_sentence(text_model, 280)
            self.assertIsNotNone(result)
