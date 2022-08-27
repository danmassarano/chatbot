"""Orchestrate chatbot to run extract, transform, and load."""
from src.data_cleanse import clean_input_files
from src.extract import get_all_tweets
from src.extract import get_api_client
from src.extract import get_output_file
from src.extract import write_to_output_file
from src.markov_chain import load_input_files
from src.markov_chain import output_sentence
from src.markov_chain import output_short_sentence
from src.markov_chain import train_text_model

output_file, writer = get_output_file("twitter_dump")
api = get_api_client()
tweets = get_all_tweets("edthewlis", api)
write_to_output_file(writer, tweets, output_file)
# get_all_tweets("elonmusk", "twitter_dump")

clean_input_files()

training_data = load_input_files()
text_model = train_text_model(training_data)

print("Print five sentences:\n")
for i in range(5):
    print(output_sentence(text_model))

print("\nPrint three sentences of no more than 280 characters:\n")
for i in range(3):
    print(output_short_sentence(text_model, 280))
