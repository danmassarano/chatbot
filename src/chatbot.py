from data_cleanse import clean_input_files
from extract import get_all_tweets
from extract import get_api_client
from extract import get_output_file
from markov_chain import load_input_files
from markov_chain import output_sentence
from markov_chain import output_short_sentence
from markov_chain import train_text_model

output_file, writer = get_output_file("twitter_dump")
api = get_api_client()
get_all_tweets("edthewlis", api, writer)
output_file.close()
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
