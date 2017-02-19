import discord
import asyncio
import traceback
import sys
from io import BytesIO, StringIO
import time

client = discord.Client()
VERSION = 'beta'

@client.event
async def on_ready():
	print('signed in as:')
	print(client.user.name)
	print(client.user.id)
	print('~~~~~~~~~~~')
	print(client)

	

@client.event
async def on_message(message):
	if message.author.id != client.user.id
		return
	if message.content.startswith('+'):
		print('Command: ' + message.content)
	command = message.content
	parameters = ' '.join(message.content.strip().split(' ')[1:])
	if command.startswith("+shutdown"):
		await reply(message, 'turning off...')
		await client.logout()
	elif command.startswith('+time'):
		await reply(message, time.ctime())

##async def reply(message, text):
##	await client.send_message(message.channel, message.author.mention + ', ' + text)

async def reply(message, text):
	await client.edit_message(message, message.author.mention + ', ' + text)

client.run('email','password')
