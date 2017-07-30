import discord
from discord import *
import asyncio
import traceback
import sys
from io import BytesIO, StringIO
import time
import config
import datetime
import math
embed = discord.embeds.Embed(colour=0xff0000)
client = discord.Client()
author_repo = 'https://github.com/steelmaker86/watchselfbot'
VERSION = '0.1'
about = (
"I am watchbot, a discord selfbot made by <@212589934966472704> that tells the\n"
"time, and I also have other random stuff. I am currently on\n"
"version: " + VERSION + ". I was made in python. I was also inspired by the\n"
"selfbot [RDT]Test made!! You can find me [HERE!]({})\n"
"".format(author_repo))
prefix = config.prefix
thoriumstatus = 'rekt'
bork = 'real'


@client.event
async def on_ready():
	startup = time.ctime()
	print('Signed in as:')
	print(client.user.name)
	print(client.user.id)
	print('~~~~~~~~~~~')
	print(client)
	print('Startup at: ' + startup)
	embed.clear_fields()

@client.event
async def on_message(message):
	prefix = config.prefix
	arguments = ' '.join(message.content.strip().split(' ')[1:])
	cmd_string_bool = message.content.startswith(prefix)
	cmd_string = message.content
	if message.author.id != client.user.id:
		return
	if cmd_string_bool:
		print('Command: {0} with arguments: {1}'.format(cmd_string, arguments))
	command = message.content
	if command.startswith(prefix + "shutdown"):
		await reply(message, 'turning off...')
		await client.logout()
	elif command.startswith(prefix + 'time'):
		await client.edit_message(message, 'The time and date is: ' + time.ctime())
	elif command.startswith(prefix +'info'):
		embed = discord.embeds.Embed(colour=0xff0000)
		embed.clear_fields
		user=client.user.name
		embed.set_author(name='Watchselfbot', url='http://github.com/steelmaker86/watchselfbot', icon_url=Embed.Empty)
		embed.add_field(name="Instance owned by:", value=user, inline=True)
		embed.add_field(name="Language", value="Python", inline=True)
		embed.add_field(name="Api Wrapper", value="Discord.py", inline=True)
		embed.add_field(name="Version", value=VERSION, inline=True)
		embed.add_field(name="About Me", value=about, inline=False)
		embed.set_footer(text="Made to help discordians since 2-19-2017!")
		embed.set_thumbnail(url='http://i.picresize.com/images/2017/03/15/TlYWM.png')
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
		 'time, shutdown, lenny, communism, ppap.\n')
	elif command.startswith(prefix + 'ppap'):
		await client.edit_message(message, "I have an apple. I have a pen. UH! Apple Pen!\n"
		"I have a pineapple. I have a pen. UH! pineapple Pen!\n"
		"Apple Pen, Pineapple Pen. UH! Pen Pineapple apple pen!\n")
	elif command.startswith(prefix + 'ping'):
		ts = message.timestamp
		new_msg = await client.edit_message(message, 'PONG!')
		latency = new_msg.edited_timestamp - ts
		if latency.microseconds >= 1000000:
			await client.edit_message(message, 'PONG! It took {} miliseconds, or {} seconds to respond!'.format(latency.microseconds // 1000, latency.microseconds / 1000000))
		else:
			await client.edit_message(message, 'PONG! It took {} miliseconds to respond!'.format(latency.microseconds // 1000))
	elif command.startswith(prefix + 'eval'):
		if arguments == '':
			await client.edit_message(message, 'Please add something to evaluate')
		else:
			output = eval(arguments)
			await client.edit_message(message, '**Input:**\n```{0}```\n**Output: **\n```{1}\n```'.format(arguments, output))
	elif command.startswith(prefix + 'cmeme'):
		embed = discord.embeds.Embed(color=0xff0000)
		embed.clear_fields()
		if arguments == '':
			client.edit_message(message, 'Please add arguments as shown: (backround picture name),(top text),(bottom text)')
		else:
			urlend = arguments.replace(',', '/')
			urlend = urlend.replace(' ', '_')
			meme = 'http://urlme.me/' + urlend
			embed.set_image(url=meme)
			embed.set_author(name='Custom Meme Generator')
			await client.edit_message(message, ' ')
			await client.edit_message(message, embed = embed)
	elif command.startswith(prefix + 'newprefix'):
		config.prefix = arguments
		client.edit_message(message, "Successfully changed prefix to: {} !".format(arguments))
	elif command.startswith(prefix + 'secretcom'):
		client.edit_message(message, "The legend of Gabe the Dog is known to be one of the few legends that is true. So one day, there was grumpy cat, a grumpy cat, and she was a meme. So then, there was a dog that was cuter than you and wanted to be a meme like grumpy cat called Gabe, so he put on obey hats and deal with it glasses by digesting Mtn. Dew and Doritos, but he didn't the respect he needed. So he listened to BE A MEME from memelan, then, he got inspired by it, so then he started barking to it like he was a dope meme more dope then you. Then he saw gravity memes. So he started to bark to it. Then, the very next day, the owner posted a DANK MEME non-clickbait youtube video of him barking. Then the memes more dank than you were posted all over social medias. Then.The best meme came. He challenged Gabe in a battle. He was almost KOed, but with his last milliter of energy. Something happened. HE 360 NOSCOPED HIM AND HE BECAME THE DANKEST MEME OF ALL THAT WILL NEVER BE DEFEATED! That is how the TRUE legend of Gabe the Dog went."

client.run(config.email, config.password)
