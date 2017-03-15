import discord
from discord import *
import asyncio
import traceback
import sys
from io import BytesIO, StringIO
import time
import config

embed = discord.embeds.Embed(colour=0xff0000)
VERSION = '0.0.6.'
about = 'I am watchbot, a discord selfbot made by <@212589934966472704> that tells the time, and I also have other random stuff. I am on version: ' + VERSION +  ' I was made in python. I was also inspired by the selfbot [RDT]Test made!! find me at: https://github.com/Steelmaker86/watchselfbot !'
client = discord.Client()
prefix = config.prefix
embed.add_field(name="Language", value="Python", inline=True)
embed.add_field(name="Api Wrapper", value="Discord.py", inline=True)
embed.add_field(name="Version", value="0.0.5", inline=True)
embed.add_field(name="About Me", value=about, inline=False)
embed.set_footer(text="Made to help discordians since 2-19-2017!")

@client.event
async def on_ready():
	startup = time.ctime()
	print('Signed in as:')
	print(client.user.name)
	print(client.user.id)
	print('~~~~~~~~~~~')
	print(client)
	print('Startup at: ' + startup)

	

@client.event
async def on_message(message):
	if message.author.id != client.user.id:
		return
	if message.content.startswith(prefix):
		print('Command: ' + message.content)
	command = message.content
	parameters = ' '.join(message.content.strip().split(' ')[1:])
	if command.startswith(prefix + "shutdown"):
		await reply(message, 'turning off...')
		await client.logout()
	elif command.startswith(prefix + 'time'):
		await client.edit_message(message, 'The time and date is: ' + time.ctime())
	elif command.startswith(prefix +'info'):
		try:
			await client.edit_message(message, " ")
			await client.edit_message(message, embed = embed)
		except discord.HTTPException:
			await client.edit_message(message, "I need the `Embed links` permission "
                               "to send this")
	elif command.startswith(prefix + 'antigrav'):
		await client.edit_message(message, 'importing the dopest antigravity memz 35%')
		time.sleep(2)
		await client.edit_message(message, 'importing the dopest antigravity memz 69%')
		time.sleep(4)
		await client.edit_message(message, 'imported the dopest antigravity memz 420%')
		import antigravity
	elif command.startswith(prefix + 'lenny'):
		await client.edit_message(message, '( ͡° ͜ʖ ͡°)')
	elif command.startswith(prefix + 'help'):
		await client.edit_message(message, 'Here are my commands, If you need some info:\n' 
		 'go to the readme.md file.\n'
		 'My commands are: antigrav, help, info,\n' 
		 'time, shutdown, lenny, and ppap\n')
	elif command.startswith(prefix + 'ppap'):
		await client.edit_message(message, "I have an pineapple. I have a pen. UH! Pinapple Pen!\n"
		"I have an apple. I have a pen. UH! Apple Pen!\n"
		"Apple Pen, Pineapple Pen. UH! Pen Pineapple apple pen!\n")

client.run(config.email, config.password)
