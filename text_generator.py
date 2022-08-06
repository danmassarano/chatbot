import csv
import json
import markovify

# TODO: Data sources are scattered across 3 subprojects - these should all be contained in a data directory
# TODO: Organise project into extract/transform/train/run structure
# TODO: requirements for this project are a mess

# TODO: Update data loader to read all files in data directory, not hardcoded strings, and handle multiple source files
# TODO: Add parameterisation to allow for a single data source
# TODO: load_teams_data should be a general 'load_from_txt' method
# TODO: load_twitter_data should be a general 'load_from_csv' method
# TODO: load_linkedin_data should be a general 'load_from_json' method

# TODO: Improve data cleanse and normalisation so it can be fully automated
# TODO: Integrate data cleanse process into load process
# TODO: Add automated way of transforming data sources to .yml

# TODO: Add makefile to build requirements and run
# TODO: Add dockerfile for chatbot
# TODO: Add tests where applicable
# TODO: Add error handling
# TODO: Add lockfile

# TODO: Refactor classes used to grab source data
# TODO: Can we make the scrapers more general or adapible?
# TODO: Can the chatbot cache/store trained data?

# TODO: Double check GitHub project settings
# TODO: Can I get a github action that automatically adds an issue if there's a todo tag?
# TODO: Linting/code formatting
# TODO: Documentation
# TODO: Readme stuff
# TODO: Add pre commit hooks to run tests, commit message, linting, requirements, documentation, etc


# Load Teams posts from Teams
def load_teams_data():
    with open("teams/ed_teams_messages.txt.clean") as f:
        teamsString = f.read()
        return teamsString


# Load Twitter posts from CSV
def load_twitter_data():
    with open("twitter/edthewlis_twitter_dump.csv.clean", newline="") as csvfile:
        twitterData = csv.reader(csvfile)
        twitterString = ""
        for row in twitterData:
            twitterString += row[0]
        return twitterString


# Load LinkedIn posts from JSON
def load_linkedin_data():
    with open("linkedin/eds-posts-text.json.clean") as json_file:
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
