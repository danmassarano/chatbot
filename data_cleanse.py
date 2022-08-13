import re
import os
from constants import INPUT_DIR


def clean_line(line):
    line = re.sub(r"http\S+", "", line)  # Remove links
    line = re.sub(r"@[^\" ]+", "", line)  # Remove usernames
    line = re.sub(r"[0-9]+", "", line)  # Remove numbers
    line = re.sub(" +", " ", line)  # Remove whitespace
    line = line.strip()

    return line


def clean_data_unstructured(filename):
    print(f"Processing {INPUT_DIR}/{filename}...", end="")
    input = open(f"{INPUT_DIR}/{filename}", "r")
    output = open(f"{INPUT_DIR}/cleaned_{filename}", "w")

    for line in input.readlines():
        new_line = clean_line(line)
        if new_line:
            output.writelines(new_line + "\n")

    input.close()
    output.close()

    print(" done")


def load_input_files():
    directory = os.fsencode(INPUT_DIR)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not (filename.startswith("cleaned")):
            if filename.endswith(".txt"):
                clean_data_unstructured(filename)
            elif filename.endswith(".csv"):
                clean_data_unstructured(filename)


load_input_files()
