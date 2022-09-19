"""Load data to a Markov Chain model and generate text."""
import markovify
from constants import CLEANED_DATA_DIR
from constants import UNSTAGED_FILE


def load_text_file(filename, dir=CLEANED_DATA_DIR):
    """
    Load a text file into memory.

    Args:
        filename (str): Name of the file to process
        dir (str), optional: Path to the input directory (default is
        CLEANED_DATA_DIR)

    Returns
        text_file_string (str): A string representation of context of file

    """
    with open(f"{dir}/{filename}") as file:
        text_file_string = file.read()
        return text_file_string


def load_input_files(dir=CLEANED_DATA_DIR, filename=UNSTAGED_FILE):
    """
    Load cleansed source file into memory.

    Args:
        dir (str), optional: Path to the input directory (default is
        CLEANED_DATA_DIR)
        filename (str), optional: Name of the source file (default is
        UNSTAGED_FILE)

    Returns
        file_string (str): A string representation of contents of file

    """
    print("Loading data...", end="")
    file_string = load_text_file(filename, dir)
    print(" done")
    return file_string


def train_text_model(training_data):
    """
    Load text into a Markov model and trains it.

    Args:
        training_data (str): Text to train the model with

    Returns
        text_model (markovify.Text): A trained Markov Chain

    """
    print("Training model...", end="")
    text_model = markovify.Text(training_data)
    print(" done\n")
    return text_model


def output_sentence(text_model):
    """
    Generate a random sentence using a Markov Chain.

    Args:
        text_model (markovify.Text): A trained Markov Chain

    Returns
        sentence (str): A random sentence

    """
    return text_model.make_sentence()


def output_short_sentence(text_model, size):
    """
    Generate a random sentence of a given length using a Markov Chain.

    Args:
        text_model (markovify.Text): A trained Markov Chain
        size (int): Maximum number of characters in a sentence

    Returns
        sentence (str): A random sentence of a given length

    """
    return text_model.make_short_sentence(size)
