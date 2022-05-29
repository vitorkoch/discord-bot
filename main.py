import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'EL GATO':
            await message.channel.send(f':elgato:')

client = MyClient()
client.run('OTgwNTI2MTgwNDA0OTY5NTQz.GB5iqM.ST79aQw7JZ4uFWCaZH487UrflBQVmK-BbEFstI')