import discord
import asyncio
import traceback
import sys
from io import BytesIO, StringIO
import time

client = discord.Client()
VERSION = '0.0.3.'

@client.event
async def on_ready():
	print('signed in as:')
	print(client.user.name)
	print(client.user.id)
	print('~~~~~~~~~~~')
	print(client)

	

@client.event
async def on_message(message):
	if message.author.id != client.user.id:
		return
	if message.content.startswith('+'):
		print('Command: ' + message.content)
	command = message.content
	parameters = ' '.join(message.content.strip().split(' ')[1:])
	if command.startswith("+shutdown"):
		await reply(message, 'turning off...')
		await client.logout()
	elif command.startswith('+time'):
		await reply(message, 'The time and date is: ' + time.ctime())
	elif command.startswith('+info'):
		await reply(message, 'I am watchbot, a discord selfbot made by Nukekin that tells the time, and I also have other random stuff. I am on version: ' + VERSION + ' I was made in python. I was also inspired by the selfbot [RDT]Test made!! find me at: https://github.com/Steelmaker86/watchselfbot !')
	elif command.startswith('+antigrav'):
		await reply(message, 'imported the dopest antigravity memz 100%')
		import antigravity
    elif command.startswith('+eval'):
        output = None
        if parameters == '':
            await reply(message, '```enter a string of code to evaluate!```')
            return
        try:
            output = eval(parameters)
        except:
            await reply(message, '```\n' + str(traceback.format_exc()) + '\n```')
            traceback.print_exc()
        if asyncio.iscoroutine(output):
            output = await output
        if output:
            await reply(message, '```\n' + str(output) + '\n```')
    elif command.startswith('+exec'):
        if parameters == '':
            await reply(message, '```enter a string of code to execute!```')
            return
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        try:
            exec(parameters)
        except Exception:
            formatted_lines = traceback.format_exc().splitlines()
            await reply(message, '```py\n{}\n{}\n```'.format(formatted_lines[-1], '\n'.join(formatted_lines[4:-1])))
            return
        finally:
            sys.stdout = old_stdout

        if redirected_output.getvalue():
            await reply(message, redirected_output.getvalue())
            return
        await reply(message, 'successfully executed code!')
        return
##async def reply(message, text):
##	await client.send_message(message.channel, message.author.mention + ', ' + text)
async def reply(message, text):
	await client.edit_message(message, message.author.mention + ', ' + text)

client.run('email','password')
