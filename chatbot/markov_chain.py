"""Load data to a Markov Chain model and generate text."""
import csv
import json
import os

import markovify
from constants import CLEANED_DATA_DIR


def load_text_file(filename, dir=CLEANED_DATA_DIR):
    """
    Load a text file into memory.

    Args:
        filename (str): Name of the file to process
        dir (str), optional: Path to the input directory (default is
        CLEANED_DATA_DIR)

    Returns
        text_file_string (str): A string representation of context of file

    """
    with open(f"{dir}/{filename}") as file:
        text_file_string = file.read()
        return text_file_string


def load_csv_file(filename, dir=CLEANED_DATA_DIR):
    """
    Load a CSV file into memory.

    Args:
        filename (str): Name of the file to process
        dir (str), optional: Path to the input directory (default is
        CLEANED_DATA_DIR)

    Returns
        csv_file_string (str): A string representation of contents of file

    """
    with open(f"{dir}/{filename}", newline="\n") as file:
        csv_file = csv.reader(file)
        csv_file_string = ""
        for row in csv_file:
            csv_file_string += row[0]
        return csv_file_string


def load_json_file(filename, text, dir=CLEANED_DATA_DIR):
    """
    Load a JSON file into memory.

    Args:
        filename (str): Name of the file to process
        dir (str), optional: Path to the input directory (default is
        CLEANED_DATA_DIR)

    Returns
        json_file_string (str): A string representation of contents of file

    """
    with open(f"{dir}/{filename}") as json_file:
        json_file = json.load(json_file)
        json_file_string = ""
        for i in range(0, len(json_file)):
            json_file_string += json_file[i][text]
        return json_file_string


def load_input_files(dir=CLEANED_DATA_DIR):
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


def train_text_model(training_data):
    """
    Load text into a Markov model and trains it.

    Args:
        training_data (str): Text to train the model with

    Returns
        text_model (markovify.Text): A trained Markov Chain

    """
    print("Training model...", end="")
    text_model = markovify.Text(training_data)
    print(" done\n")
    return text_model


def output_sentence(text_model):
    """
    Generate a random sentence using a Markov Chain.

    Args:
        text_model (markovify.Text): A trained Markov Chain

    Returns
        sentence (str): A random sentence

    """
    return text_model.make_sentence()


def output_short_sentence(text_model, size):
    """
    Generate a random sentence of a given length using a Markov Chain.

    Args:
        text_model (markovify.Text): A trained Markov Chain
        size (int): Maximum number of characters in a sentence

    Returns
        sentence (str): A random sentence of a given length

    """
    return text_model.make_short_sentence(size)
