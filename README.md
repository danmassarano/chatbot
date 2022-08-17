# Chatbot

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tag Version](https://github.com/danmassarano/chatbot/actions/workflows/tag_version.yml/badge.svg)](https://github.com/danmassarano/chatbot/actions/workflows/tag_version.yml)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

Builds a message generator and chatbot based on training data scraped from a
given person's social media.

Currently only supports Twitter

## Usage

You'll need a twitter developers API key to run the extract module. Add the
bearer token to your environment to get going

```sh
pip install -r requirements.txt
python src/chatbot.py
```

Scrapes the web and stores data in `./input` directory which is then cleaned
and loaded into `markov_chain` any outputs a given number of sentences

## Development

To run all tests:

```sh
python -m unittest discover -v -s tests
coverage run -m unittest discover -v -s tests
coverage html
black .
bandit -r src
pre-commit run --all-files
```
