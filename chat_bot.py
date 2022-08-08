from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Ed Fauxlis")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("input/*.yml")

while True:
    print("\nWhat would you like to ask?\n")
    question = input()
    print(chatbot.get_response(question))
