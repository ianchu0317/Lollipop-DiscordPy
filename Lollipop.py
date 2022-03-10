#!/usr/bin/env python3

import discord
from src.Images import Image
from src.Random import Random
from src.Chat import Chatbot
from src.News import News
from src import Info

client = discord.Client()
command_list = ['$chat', '$img', '$random', '$help', '$waifu', '$news', '$meme']

# Check if enetered message is a command
def check_command(message):
	if message.content.split(" ")[0] in command_list:
		return True
	return False

# When bot is connected
@client.event
async def on_ready():
	print("Client is online!")
	print("Client is {0}".format(client.user))

# Main function, listen to new commands
@client.event
async def on_message(message):
	isCommand = check_command(message)
	if message.author != client.user and isCommand:
		response = find_response(message)
		await message.channel.send(response)

# Check response
def find_response(message):
	command = message.content.split(" ")[0]
	if command == "$chat":
		return  '<@{}>'.format(message.author.id) + " " + Chatbot.getResponse(message.author.name, message.content.split(" ")[1:])

	elif command == "$help":
		return Info.display_menu()

	elif command == "$img":
		return Image.get_image(message.content.split(" ")[1:])

	elif command == "$random":
		return Random.find_random()

	elif command == "$news":
		msg = message.content.split(" ")
		if len(msg) < 4:
			return "$news <query> <searchIn> <language>"
		return News.getNews(msg[1], msg[2], msg[3])

if __name__ == '__main__':
	client.run('OTQwNjg1MDA5MDAwNDk3MTUy.YgK_Lw.FCd0M1YxAxXFtnVhc7aA3OyoX20')
