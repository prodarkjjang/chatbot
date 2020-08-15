from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbotname = "Brandon"
chatbot = ChatBot(chatbotname)

print(chatbotname + ": May i know how to address you dear?")


message = None
while message == None:
    name = input("You: ")
    if name.strip() != "":
        message = chatbot.get_response("My name is")
    else:
        print(chatbotname + ": Come on, I'm sure everyone has a name. Tell me yours, pretty please.")


print(chatbotname+ ": " + message.text + " " + name.capitalize() + ".")

while 1:
    userinput = input("You: ")
    if userinput == "bb":
        print("Goodbye " + name)
        break
    else:
        message = chatbot.get_response(userinput)
        print(message)
