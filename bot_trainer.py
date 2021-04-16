from chatterbot import ChatBot
from chatbot import chatbot

import chatterbot.utils
from chatterbot.trainers import ListTrainer
chatbot = ChatBot('Training Example')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Greetings!",
    "Hello",
])