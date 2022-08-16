import re
import os
from src.constants import RAW_DATA_DIR, CLEANED_DATA_DIR


def clean_line(line):
    line = re.sub(r"http\S+", "", line)  # Remove links
    line = re.sub(r"@[^\" ]+", "", line)  # Remove usernames
    line = re.sub(r"[0-9]+", "", line)  # Remove numbers
    line = re.sub(" +", " ", line)  # Remove whitespace
    line = line.strip()

    return line


def clean_data_unstructured(
    filename, in_dir=RAW_DATA_DIR, out_dir=CLEANED_DATA_DIR
):
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
    directory = os.fsencode(in_dir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            clean_data_unstructured(filename, in_dir, out_dir)
        elif filename.endswith(".csv"):
            clean_data_unstructured(filename, in_dir, out_dir)
