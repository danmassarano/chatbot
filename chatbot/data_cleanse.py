"""Cleanse extracted data to output natural language."""
import os
import re

from constants import CLEANED_DATA_DIR
from constants import RAW_DATA_DIR


def clean_line(line):
    """
    Remove links, usernames, numbers, and whitespace from a line of text.

    Args:
        line (str): A line of raw text data

    Returns
        line (str): A line of cleansed text data

    """
    line = re.sub(r"http\S+", "", line)  # Remove links
    line = re.sub(r"@[^\" ]+", "", line)  # Remove usernames
    line = re.sub(r"[0-9]+", "", line)  # Remove numbers
    line = re.sub(" +", " ", line)  # Remove whitespace
    line = line.strip()

    return line


def clean_data_unstructured(
    filename, in_dir=RAW_DATA_DIR, out_dir=CLEANED_DATA_DIR
):
    """
    Create a new file of cleansed text given a raw data file.

    Args:
        filename (str): Name of the file to process
        in_dir (str), optional: Path to the input directory (default is
        RAW_DATA_DIR)
        out_dir (str), optional: Path to the output directory (default is
        CLEANED_DATA_DIR)

    Returns
        None

    """
    print(f"Processing {filename}...", end="")
    input = open(f"{in_dir}/{filename}", "r")
    output = open(f"{out_dir}/{filename}", "w")

    for line in input.readlines():
        new_line = clean_line(line)
        if new_line:
            output.writelines(new_line + "\n")

    input.close()
    output.close()

    print(" done")


def clean_input_files(in_dir=RAW_DATA_DIR, out_dir=CLEANED_DATA_DIR):
    """
    Cleanse all files in a directory, creating processed files for each.

    Args:
        in_dir (str), optional: Path to the input directory (default is
        RAW_DATA_DIR)
        out_dir (str), optional: Path to the output directory (default is
        CLEANED_DATA_DIR)

    Returns
        None

    """
    directory = os.fsencode(in_dir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            clean_data_unstructured(filename, in_dir, out_dir)
        elif filename.endswith(".csv"):
            clean_data_unstructured(filename, in_dir, out_dir)
