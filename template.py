import discord
from os import linesep as br  # Break line


def read(message):
    return message.content.strip().lower()


class MyClient(discord.Client):
    async def on_ready(self):
        print('=-' * 10)
        print(f'Bot {self.user} ON!')
        print('=-' * 10)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


client = MyClient()
client.run('insira seu token aqui')
