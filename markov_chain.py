import csv
import json

import markovify


# Load Teams posts from Teams
def load_teams_data():
    with open("input/ed_teams_messages.txt.clean") as f:
        teamsString = f.read()
        return teamsString


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


teams = load_teams_data()
twitter = load_twitter_data()
linkedin = load_linkedin_data()

# Build the model
text_model = markovify.Text(teams + twitter + linkedin)

# Print five randomly-generated sentences
print("Print five randomly-generated sentences:\n")
for i in range(5):
    print(text_model.make_sentence())

# Print three randomly-generated sentences of no more than 280 characters
print("\nPrint three randomly-generated sentences of no more than 280 characters:\n")
for i in range(3):
    print(text_model.make_short_sentence(280))
