# Chatbot

[![CI](https://github.com/danmassarano/chatbot/actions/workflows/CI.yml/badge.svg)](https://github.com/danmassarano/chatbot/actions/workflows/CI.yml)
[![coverage](https://github.com/danmassarano/chatbot/blob/main/.github/badges/coverage_badge.svg)](https://coverage.readthedocs.io/en/6.4.4/)
[![docs](https://github.com/danmassarano/chatbot/blob/main/.github/badges/interrogate_badge.svg)](https://interrogate.readthedocs.io/en/latest/?badge=latest)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![dependencies](https://github.com/danmassarano/chatbot/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/danmassarano/chatbot/actions/workflows/dependency-review.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

Builds a message generator and chatbot based on training data scraped from a
given person's social media.

Currently only supports Twitter

## Usage

You'll need a twitter developers API key to run the extract module. Add the
bearer token to your environment to get going

```sh
make setup
make run
```

Scrapes the web and stores data in `./input` directory which is then cleaned
and loaded into `markov_chain` any outputs a given number of sentences

## Development

To run all tests:

```sh
make test
```
