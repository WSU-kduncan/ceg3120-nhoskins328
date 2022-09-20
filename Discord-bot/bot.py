import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    panther_players = [
        'Luke Kuechly',
        'Greg Olsen',
        'Steve Smith',
        'Cam Newton',
        'Brian Burns',
        'Julius Peppers',
        'Sam Mills',
        'Jeremy Chinn',
        'Jordan Gross',
        'Josh Norman',
        'DJ Moore',
        'Christain McCaffery',
        'Shaq Thompson',
        'Jonathan Stewart',
        'Thomas Davis',
        'Jake Delhomme',
        'Ryan Kalil',
        'John Fox',
        'Ron Rivera',
    ]

    if message.content == 'panther!':
        response = random.choice(panther_players)
        await message.channel.send(response)
        return

client.run(TOKEN)
