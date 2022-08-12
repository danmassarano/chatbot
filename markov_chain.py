import csv
import json

import markovify


def load_text_file(filename):
    with open("./input/" + filename + ".txt") as file:
        text_file_string = file.read()
        return text_file_string


def load_csv_file(filename):
    with open("./input/" + filename + ".csv", newline="") as file:
        csv_file = csv.reader(file)
        csv_file_string = ""
        for row in csv_file:
            csv_file_string += row[0]
        return csv_file_string


def load_json_file(filename, text):
    with open("./input/" + filename + ".json") as json_file:
        json_file = json.load(json_file)
        json_file_string = ""
        for i in range(0, len(json_file)):
            json_file_string += json_file[i][text]
        return json_file_string


text_file_string = load_text_file("ed_teams_messages")
csv_file_string = load_csv_file("edthewlis_twitter_dump")
json_file_string = load_json_file("eds-posts-text", "text")


print("Training model...")
text_model = markovify.Text(text_file_string + csv_file_string + json_file_string)

# Print five randomly-generated sentences
print("Print five randomly-generated sentences:\n")
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
print("\nPrint three randomly-generated sentences of no more than 280 characters:\n")
for i in range(3):
    print(text_model.make_short_sentence(280))
