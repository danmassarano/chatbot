"""test_constants overrides constants when running tests."""
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CLEANED_DATA_DIR = f"{DIR_PATH}/fixtures/data/cleaned"
STAGING_DATA_DIR = f"{DIR_PATH}/fixtures/data/staging"
RAW_DATA_DIR = f"{DIR_PATH}/fixtures/data/raw"
EXPECTED_DATA_DIR = f"{DIR_PATH}/fixtures/data/expected"
UNSTAGED_FILE = "input_data.txt"
