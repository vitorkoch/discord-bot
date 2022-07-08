import discord
from os import linesep as br  # Break Line
from Token import token # Arquivo apenas com uma variável chamada token com meu token do discord

def read(message):
    return message.content.strip().lower()


class MyClient(discord.Client):
    async def on_ready(self):
        print('=-' * 10)
        print(f'Bot {self.user} ON!')
        print('=-' * 10)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if read(message) == '!regras':
            await message.channel.send(
                f'As regras do servidor são:{br}Regra 1: Não desrespeitar os membros{br}Regra 2: blá blá blá'
            )
        if read(message) == 'el gato':
            await message.channel.send(file=discord.File('elgato/elgato.jpg'))
        if read(message) == 'if' or read(message) == 'ifpa':
            await message.channel.send('Destruidor de saúde mental')
        if read(message) == 'boa noite':
            await message.channel.send(file=discord.File('images/boanoite.jpeg'))
        if (
            read(message) == 'chama todo mundo'
            or read(message) == 'el gato chama todo mundo'
        ):
            await message.channel.send('@everyone, vem aqui')
        if read(message) == '!chika':
            await message.channel.send(file=discord.File('images/chika.gif'))


client = MyClient()
client.run(token)
