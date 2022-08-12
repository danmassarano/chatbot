# Chatbot

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Builds a message generator and chatbot based on training data scraped from a given person's social media.

Currently only supports Twitter

## Usage

```sh
pip install -r requirements.txt
python extract.py
python data_cleanse.py
python markov_chain.py
```

Scrapes the web and stores data in `./input` directory which is then cleaned and loaded into either `markov_chain` or `chat_bot`.
