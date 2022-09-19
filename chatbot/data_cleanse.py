"""Cleanse extracted data to output natural language."""
import csv
import json
import os
import re

from constants import CLEANED_DATA_DIR
from constants import RAW_DATA_DIR
from constants import STAGING_DATA_DIR
from constants import UNSTAGED_FILE


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
    line = re.sub(
        r"(#|/|\(|\)|\{|\}|\[|\]|_|-|=|\+|^|&|\*|`|~|<|>|£|$)+", "", line
    )  # Remove extra punctuation
    line = re.sub(r"[0-9]+", "", line)  # Remove numbers
    line = re.sub(" +", " ", line)  # Remove whitespace
    line = line.strip()

    return line


def clean_data_unstructured(
    filename, in_dir=RAW_DATA_DIR, out_dir=STAGING_DATA_DIR
):
    """
    Create a new file of cleansed text given a raw data file.

    Args:
        filename (str): Name of the file to process
        in_dir (str), optional: Path to the input directory (default is
        RAW_DATA_DIR)
        out_dir (str), optional: Path to the output directory (default is
        STAGING_DATA_DIR)

    Returns
        None

    """
    print(f"Processing {filename}...", end="")
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    input = open(f"{in_dir}/{filename}", "r")
    output = open(f"{out_dir}/{filename}", "w")

    for line in input.readlines():
        new_line = clean_line(line)
        if new_line:
            output.writelines(new_line + "\n")

    input.close()
    output.close()

    print(" done")


def clean_input_files(in_dir=RAW_DATA_DIR, out_dir=STAGING_DATA_DIR):
    """
    Cleanse all files in a directory, creating processed files for each.

    Args:
        in_dir (str), optional: Path to the input directory (default is
        RAW_DATA_DIR)
        out_dir (str), optional: Path to the output directory (default is
        STAGING_DATA_DIR)

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


def load_text_file(filename, dir=STAGING_DATA_DIR):
    """
    Load a text file into memory.

    Args:
        filename (str): Name of the file to process
        dir (str), optional: Path to the input directory (default is
        STAGING_DATA_DIR)

    Returns
        text_file_string (str): A string representation of context of file

    """
    with open(f"{dir}/{filename}") as file:
        text_file_string = file.read()
        return text_file_string


def load_csv_file(filename, dir=STAGING_DATA_DIR):
    """
    Load a CSV file into memory.

    Args:
        filename (str): Name of the file to process
        dir (str), optional: Path to the input directory (default is
        STAGING_DATA_DIR)

    Returns
        csv_file_string (str): A string representation of contents of file

    """
    with open(f"{dir}/{filename}", newline="\n") as file:
        csv_file = csv.reader(file)
        csv_file_string = ""
        for row in csv_file:
            csv_file_string += row[0]
        return csv_file_string


def load_json_file(filename, text, dir=STAGING_DATA_DIR):
    """
    Load a JSON file into memory.

    Args:
        filename (str): Name of the file to process
        dir (str), optional: Path to the input directory (default is
        STAGING_DATA_DIR)

    Returns
        json_file_string (str): A string representation of contents of file

    """
    with open(f"{dir}/{filename}") as json_file:
        json_file = json.load(json_file)
        json_file_string = ""
        for i in range(0, len(json_file)):
            json_file_string += json_file[i][text]
        return json_file_string


def load_input_files(dir=STAGING_DATA_DIR):
    """
    Load all files in a directory into memory.

    Args:
        dir (str), optional: Path to the input directory (default is
        CLEANED_DATA_DIR)

    Returns
        file_string (str): A string representation of contents of files

    """
    print("Loading data...", end="")
    directory = os.fsencode(dir)
    file_string = ""
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            file_string += load_text_file(filename, dir)
        elif filename.endswith(".csv"):
            file_string += load_csv_file(filename, dir)
        elif filename.endswith(".json"):
            file_string += load_json_file(filename, "text", dir)
        print(" done")
    return file_string


def unstage_cleansed_files(
    in_dir=STAGING_DATA_DIR,
    out_dir=CLEANED_DATA_DIR,
    output_file=UNSTAGED_FILE,
):
    """
    Join all cleansed files into a single output file.

    Args:
        in_dir (str), optional: Path to the input directory (default is
        STAGING_DATA_DIR)
        out_dir (str), optional: Path to the output directory (default is
        CLEANED_DATA_DIR)
        output_file (str), optional: Name of the final output file (default is
        UNSTAGED_FILE)

    Returns
        None

    """
    print("Unstaging data...", end="")
    final_file_string = load_input_files(in_dir)
    with open(f"{out_dir}/{output_file}", "w") as output:
        output.writelines(final_file_string + "\n")
    output.close()
    print(" done")
