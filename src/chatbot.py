from src.extract import get_all_tweets
from src.data_cleanse import clean_input_files
from src.markov_chain import (
    train_text_model,
    output_sentence,
    output_short_sentence,
)


get_all_tweets("edthewlis", "twitter_dump")
# get_all_tweets("elonmusk", "twitter_dump")
clean_input_files()

text_model = train_text_model()

print("Print five sentences:\n")
for i in range(5):
    print(output_sentence(text_model))

print("\nPrint three sentences of no more than 280 characters:\n")
for i in range(3):
    print(output_short_sentence(text_model, 280))
