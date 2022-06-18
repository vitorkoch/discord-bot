import discord
from os import linesep as br  # Break Line


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
        if read(message) == 'if' or message.content == 'ifpa':
            await message.channel.send('Destruidor de saúde mental')
        if read(message) == 'boa noite':
            await message.channel.send(file=discord.File('images/boanoite.jpeg'))
        if read(message) == 'el gato bebe':
            await message.channel.send('<:elgato:977977352409722910>')
        if read(message) == '!weka':
            await message.channel.send(
                f'@{message.author}, Aqui: https://docs.google.com/spreadsheets/d/1u043DjKpAY6tLJDxC7WieIYLFZZficPzeseuwvJ88j8/edit?usp=sharing'
            )
        if (
            read(message) == 'chama todo mundo'
            or read(message) == 'el gato chama todo mundo'
        ):
            await message.channel.send('@everyone, vem aqui')
        if read(message) == '!chika':
            await message.channel.send(file=discord.File('images/chika.gif'))


client = MyClient()
client.run('OTgwNTI2MTgwNDA0OTY5NTQz.GwWMf1.s_4jVauK81cFkamgeVwyRKnAHgFzjV1Bpdm5lc')
