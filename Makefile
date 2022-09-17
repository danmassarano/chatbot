PYTHON = python3.9

.PHONY = help env test run clean

.DEFAULT_GOAL = help

help:
	@echo "---------------------HELP-----------------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "To check pre-commit hook type make pre-commit"
	@echo "------------------------------------------------"

env:
	@python3.9 -m venv ./venv
	@. venv/bin/activate

setup: env
	@pip install -r requirements.txt
	@pre-commit autoupdate

pre-commit:
	@pre-commit run --all-files

test:
	@coverage run -m unittest discover -v -s tests
	@coverage html

run:
	@${PYTHON} chatbot/chatbot.py

clean:
	@rm -rf venv
	@find -iname "*.pyc" -delete
