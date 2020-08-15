from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Brandon')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi there!",
    "Hello",
])

trainer.train([
    "Greetings!",
    "Hello",
])

trainer.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])

trainer.train([
    "My name is",
    "Hi, nice to meet you",
])

trainer.train([
    "My name is",
    "Hi, how are you doing",
])


