import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/genderroll'):
        def random_line(fname):
            lines = open(fname).read().splitlines()
            return random.choice(lines)
     
        await message.channel.send('Your gender of the day is: ' + random_line('genders.txt'))


my_secret = os.environ['TOKEN']
client.run(my_secret)
