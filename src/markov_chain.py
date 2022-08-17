import csv
import json
import os

import markovify

from src.constants import CLEANED_DATA_DIR


def load_text_file(filename, dir=CLEANED_DATA_DIR):
    with open(f"{dir}/{filename}") as file:
        text_file_string = file.read()
        return text_file_string


def load_csv_file(filename, dir=CLEANED_DATA_DIR):
    with open(f"{dir}/{filename}", newline="\n") as file:
        csv_file = csv.reader(file)
        csv_file_string = ""
        for row in csv_file:
            csv_file_string += row[0]
        return csv_file_string


def load_json_file(filename, text, dir=CLEANED_DATA_DIR):
    with open(f"{dir}/{filename}") as json_file:
        json_file = json.load(json_file)
        json_file_string = ""
        for i in range(0, len(json_file)):
            json_file_string += json_file[i][text]
        return json_file_string


def load_input_files(dir=CLEANED_DATA_DIR):
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
    return file_string


# TODO: Refactor to take a string input
# This should just take a string input and the data load calls should be
# handled in the chatbot module
# labels: refactor
# assignees: danmassarano
def train_text_model(dir=CLEANED_DATA_DIR):
    print("Loading data...", end="")
    file_string = load_input_files(dir)
    print(" done")

    print("Training model...", end="")
    text_model = markovify.Text(file_string)
    print(" done\n")
    return text_model


def output_sentence(text_model):
    return text_model.make_sentence()


def output_short_sentence(text_model, size):
    return text_model.make_short_sentence(size)
