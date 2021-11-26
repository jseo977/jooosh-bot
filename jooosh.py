# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    msg = message
    if msg.author == client.user:
        return

    unethiquotes = [
        'Happy Birthday Stephen!',
        'But wa',
        '...Boo!\n Woah, I almost fell off my chair',
        'Iiiiiiiiincredible',
        'I\'m Jooosh and I\'m from Christchurch',
        'Oh guys \'joooshbag\' is already taken',
        'You wouldn\'t get it',
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley',
        'I also do linguistics',
        'Ohhhh, right',
        'I can\'t produce under pressure... you need to observe me',
        '*Meme reference*',
        'skmssdksdmk',
        ':sobeautiful:',
        'I don\'t listen to music when I shower',
        'Stellaaaaaaaaaaaaa',
        '*Keyboard Smash*',
        'Horny bonk!'
    ]
    psr = ['paper 📄',' Scissors ✂️','Rock 🗿']

    if msg.content == 'psr!':
        poopy = random.choice(psr)
        await msg.channel.send(poopy)

    if msg.content == 'flip!coin':
        poop = random.choice(['Heads 🍆','Tails 💦'])
        await msg.channel.send(poop)

    if msg.content == 'josh!help':
        await msg.channel.send(
        ('Commands:\n'
        'josh!quotes: Josh Quotes\n'
        'josh!taunt: Random capitalisation on string\n'
        'josh!what: Sends a random number of \'What\'s\n',
        'flip!coin: flips a coin\n'
        'psr!: Paper, scissors, rock'
        )
        )

    if msg.content.startswith("josh!"):
        if msg.content.startswith('josh!quotes'):
            response = random.choice(unethiquotes)
            await msg.channel.send(response)

        if msg.content.startswith("josh!taunt"):
            key = msg.content.lstrip("josh!taunt")
            await msg.channel.send(''.join(random.choice((str.upper, str.lower))(c) for c in key))

        if msg.content.startswith("josh!what"):
            msgs = msg.content.split(' ')
            if len(msgs) == 1:
                await msg.channel.send("What"*random.randint(1,100))
            elif len(msgs) == 2 & int(msgs[1]):
                await msg.channel.send("What"*int(msgs[1]))

    if msg.content == "Stephen!":
        await msg.channel.send("Hello, Stephen \nWe missed you")

    if msg.content == "Asmitha!":
        await msg.channel.send("Hello, Asmitha \nWe missed you")
    
    if msg.content == "Stella!":
        await msg.channel.send("Hello, Stella \nWe missed you")


client.run(TOKEN)