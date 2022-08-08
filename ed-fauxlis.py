#!/usr/bin/env python3

import json

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot("Ed Fauxlis")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("text")

while True:
    print("\nWhat would you like to ask?\n")
    question = input()
    print(chatbot.get_response(question))
