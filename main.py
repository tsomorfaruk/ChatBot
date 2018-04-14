from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Bot') #create the chatbot
bot.set_trainer(ListTrainer)#set trainer
for _file in os.listdir('files'):
	data = open('files/' + _file , 'r').readlines()

	bot.train(data)

while True:
	message = input('me: ')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Bot: ',reply)
	if message.strip() == 'Bye':
		print('Bot: Bye')
		break
	if message.strip() == 'bye':
		print('Bot: Bye')
		break
