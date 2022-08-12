import csv
import json

import markovify


def load_text_file(filename):
    with open("./input/" + filename + ".txt") as file:
        text_file_string = file.read()
        return text_file_string


# Load Twitter posts from CSV
def load_twitter_data():
    with open("input/edthewlis_twitter_dump.csv.clean", newline="") as csvfile:
        twitterData = csv.reader(csvfile)
        twitterString = ""
        for row in twitterData:
            twitterString += row[0]
        return twitterString


# Load LinkedIn posts from JSON
def load_linkedin_data():
    with open("input/eds-posts-text.json.clean") as json_file:
        linkedinData = json.load(json_file)
        linkedinString = ""
        for i in range(0, len(linkedinData)):
            linkedinString += linkedinData[i]["text"]
        return linkedinString


text_file = load_text_file("ed_teams_messages")
# twitter = load_twitter_data()
# linkedin = load_linkedin_data()

# # Build the model
# text_model = markovify.Text(teams + twitter + linkedin)
text_model = markovify.Text(text_file)

# Print five randomly-generated sentences
print("Print five randomly-generated sentences:\n")
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
print("\nPrint three randomly-generated sentences of no more than 280 characters:\n")
for i in range(3):
    print(text_model.make_short_sentence(280))
