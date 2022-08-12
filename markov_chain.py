import csv
import json
import os
from constants import *

import markovify


def load_text_file(filename):
    with open(f"{INPUT_DIR}/{filename}") as file:
        text_file_string = file.read()
        return text_file_string


def load_csv_file(filename):
    with open(f"{INPUT_DIR}/{filename}", newline="\n") as file:
        csv_file = csv.reader(file)
        csv_file_string = ""
        for row in csv_file:
            csv_file_string += row[0]
        return csv_file_string


def load_json_file(filename, text):
    with open(f"{INPUT_DIR}/{filename}") as json_file:
        json_file = json.load(json_file)
        json_file_string = ""
        for i in range(0, len(json_file)):
            json_file_string += json_file[i][text]
        return json_file_string


def load_input_files():
    directory = os.fsencode(INPUT_DIR)
    file_string = ""
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith("cleaned"):
            if filename.endswith(".txt"):
                file_string += load_text_file(filename)
            elif filename.endswith(".csv"):
                file_string += load_csv_file(filename)
            elif filename.endswith(".json"):
                file_string += load_json_file(filename, "text")
    return file_string


print("Loading data...", end="")
file_string = load_input_files()
print(" done")

print(file_string)

print("Training model...", end="")
text_model = markovify.Text(file_string)
print(" done\n")

# Print five randomly-generated sentences
print("Print five randomly-generated sentences:\n")
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
print("\nPrint three randomly-generated sentences of no more than 280 characters:\n")
for i in range(3):
    print(text_model.make_short_sentence(280))
