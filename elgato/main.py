import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '!regras':
            await message.channel.send(f'As regras do servidor são:{os.linesep}Regra 1: Não desrespeitar os membros{os.linesep}Regra 2: blá blá blá')
        if message.content == 'el gato':
            await message.channel.send(file=discord.File('elgato.jpg'))
        if message.content == 'if' or message.content == 'ifpa':
            await message.channel.send('Uma merda')
        if message.content == 'boa noite':
            await message.channel.send(file=discord.File('images/boanoite.jpeg'))

client = MyClient()
client.run('OTgwNTI2MTgwNDA0OTY5NTQz.GG80_a.GMAjovO7yOFNQGREwe2ReBlWuqmtNFRlJFxWU4')