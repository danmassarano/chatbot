# ed_faux_list

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Scraping of Ed's MS Teams and/or social media messages and building an Ed message generator to pass a Turing Test

## `chatterbot`

Uses the corpuses…corpi…corpora…files located in the `text` directory.

`chatterbot` requires Python 3.6 and some specific versions of dependencies:

```sh
python3 -m pip install chatterbot
python3 -m pip install spacy==2.1.9
python3 -m spacy download en
python3 -m pip install pyyaml==5.4.1
```

After that, run:

```sh
./ed-fauxlis.py
```

## data cleaning

* remove urls
* remove @<username>
* remove things wrapped in brackets
* remove non-printing unicode
* remove hashtags
* remove ellipsis
