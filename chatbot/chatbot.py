"""Orchestrate chatbot to run extract, transform, and load."""
import argparse
import sys

from data_cleanse import clean_input_files
from data_cleanse import unstage_cleansed_files
from extract import get_all_tweets
from extract import get_api_client
from extract import get_output_file
from extract import write_to_output_file
from markov_chain import load_input_files
from markov_chain import output_sentence
from markov_chain import output_short_sentence
from markov_chain import train_text_model


def main(argv=None):
    """
    Run the chatbot given a username.

    Args:
        argv (-u, --username): Any arguments passed in at runtime

    """
    parser = argparse.ArgumentParser(
        description="Builds a message chatbot using a markov chain"
    )
    parser.add_argument(
        "-u",
        "--username",
        help="Username of person to mimic",
        required=False,
        default="",
    )

    argument = parser.parse_args(argv)
    username = ""

    if argument.username:
        username = "{0}".format(argument.username)
    else:
        while username == "":
            username = input(
                "What's the twitter username we're impersonating "
                "(without the @)? "
            )

    output_file, writer = get_output_file("twitter_dump")
    api = get_api_client()
    tweets = get_all_tweets(username, api)
    write_to_output_file(writer, tweets, output_file)

    clean_input_files()
    unstage_cleansed_files()

    training_data = load_input_files()
    text_model = train_text_model(training_data)

    print("Print five sentences:\n")
    for _ in range(5):
        print(output_sentence(text_model))

    print("\nPrint three sentences of no more than 280 characters:\n")
    for _ in range(3):
        print(output_short_sentence(text_model, 280))


if __name__ == "__main__":
    sys.exit(main())
