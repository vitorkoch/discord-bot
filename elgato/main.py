import discord
import os

# TODO => Deixar o bot ON
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Bot {self.user} ON!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content == '!regras':
            await message.channel.send(
                f'As regras do servidor são:{os.linesep}Regra 1: Não desrespeitar os membros{os.linesep}Regra 2: blá blá blá'
            )
        if message.content == 'el gato':
            await message.channel.send(file=discord.File('elgato/elgato.jpg'))
        if message.content == 'if' or message.content == 'ifpa':
            await message.channel.send('Uma merda')
        if message.content == 'boa noite':
            await message.channel.send(file=discord.File('images/boanoite.jpeg'))
        if message.content == 'el gato bebe':
            await message.channel.send('<:elgato:977977352409722910>')
        if message.content == '!weka':
            await message.channel.send(
                f'@{message.author}, Aqui: https://docs.google.com/spreadsheets/d/1u043DjKpAY6tLJDxC7WieIYLFZZficPzeseuwvJ88j8/edit?usp=sharing'
            )
        if message.content == 'chama todo mundo':
            await message.channel.send('@everyone, vem aqui')
        if message.content == 'gay':
            await message.channel.send(f'Tu que é gay {message.author}')


client = MyClient()
client.run('OTgwNTI2MTgwNDA0OTY5NTQz.GwWMf1.s_4jVauK81cFkamgeVwyRKnAHgFzjV1Bpdm5lc')
