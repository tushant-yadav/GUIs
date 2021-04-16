from chatterbot.trainers import *
from chatterbot import ChatBot
'''bot=ChatBot('Test')
conv = open('chats.txt','r').readlines()
bot.set_trainer(ListTrainer)
bot.train(conv)

while True:
	request= input('You: ')
	response = bot.get_response(request)
	print('Bot: ', response)



'''
#from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")	
while True:
	request= input('You: ')
	response = chatbot.get_response(request)
	print('Bot: ', response)
