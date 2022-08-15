import unittest

from os.path import exists

from data_cleanse import clean_line, clean_data_unstructured, clean_input_files
from tests.test_constants import (
    CLEANED_DATA_DIR,
    RAW_DATA_DIR,
    EXPECTED_DATA_DIR,
)


class TestDataCleanse(unittest.TestCase):
    def test_clean_line(self):
        """
        Test that cleaning a single line works as expected
        """
        line = "@OffMenuOfficial thoughts, chaps? https://t.co/Am7Lpdc74Q"
        expected = "thoughts, chaps?"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_links(self):
        """
        Test that links are removed
        """
        line = "Here https://t.co/Am7Lpdc74Q"
        expected = "Here"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_username(self):
        """
        Test that usernames are removed
        """
        line = "@OffMenuOfficial thoughts"
        expected = "thoughts"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_usernames(self):
        """
        Test that multiple usernames are removed
        """
        line = "@YAhkter @KaneFulton @DataShedAnna I think"
        expected = "I think"
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_line_numbers(self):
        """
        Test that numbers are removed
        """
        line = "1234"
        expected = ""
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_whitespace(self):
        """
        Test that extra whitespace is removed
        """
        line = "    "
        expected = ""
        result = clean_line(line)
        self.assertEqual(result, expected)

    def test_clean_csv_file(self):
        """
        Tests that csv file is processed correctly
        """
        filename = "test_csv.csv"
        clean_data_unstructured(filename, RAW_DATA_DIR, CLEANED_DATA_DIR)

        expected_file = open(f"{EXPECTED_DATA_DIR}/{filename}", "r")
        expected = expected_file.read()
        expected_file.close()

        result_file = open(f"{CLEANED_DATA_DIR}/{filename}", "r")
        result = result_file.read()
        result_file.close()

        self.assertEqual(result, expected)

    def test_clean_text_file(self):
        """
        Tests that text file is processed correctly
        """
        filename = "test_txt.txt"
        clean_data_unstructured(filename, RAW_DATA_DIR, CLEANED_DATA_DIR)

        expected_file = open(f"{EXPECTED_DATA_DIR}/{filename}", "r")
        expected = expected_file.read()
        expected_file.close()

        result_file = open(f"{CLEANED_DATA_DIR}/{filename}", "r")
        result = result_file.read()
        result_file.close()

        self.assertEqual(result, expected)

    def test_clean_input_files(self):
        """
        Tests that all files are processed
        """
        clean_input_files(RAW_DATA_DIR)

        expected_txt = f"{CLEANED_DATA_DIR}/test_txt.txt"
        expected_csv = f"{CLEANED_DATA_DIR}/test_csv.csv"

        self.assertTrue(exists(expected_txt))
        self.assertTrue(exists(expected_csv))


if __name__ == "__main__":
    unittest.main()
