# bot.py
import random

import discord
from keep_alive import keep_alive

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('jooosh-bot is alive!')

@client.event
async def on_message(message):
    msg = message
    if msg.author == client.user:
        return

    with open("josh_quotes.txt") as file:
        unethiquotes = file.readlines()

    psr = ['paper 📄',' Scissors ✂️','Rock 🗿']

    if msg.content == 'psr!':
        poopy = random.choice(psr)
        await msg.channel.send(poopy)

    if msg.content == 'flip!coin':
        poop = random.choice(['Heads 🍆','Tails 💦'])
        await msg.channel.send(poop)

    if msg.content == 'josh!help':
        await msg.channel.send(
        'Commands:\njosh!quotes: Josh Quotes\njosh!add: Add quote\njosh!delete: delete quote\njosh!latest: Sends the latest quote\njosh!taunt: Random capitalisation on string\njosh!what: Sends a random number of \'What\'s\nflip!coin: flips a coin\npsr!: Paper, scissors, rock'
        )

    if msg.content.startswith("josh!"):
        if msg.content == 'josh!quotes':
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

        if msg.content.startswith('josh!add'):
            with open("josh_quotes.txt", "r+") as file:
                file.write(f"{msg.content.lstrip('josh!add ')}\n")
                unethiquotes = file.readlines()
            await msg.channel.send(f"Learning: {msg.content.lstrip('josh!add')}")

        if msg.content.startswith('josh!delete'):
            with open("josh_quotes.txt", "r+") as file:
                quotes = file.readlines()
                file.seek(0)
                for quote in quotes:
                    if quote != msg.content.lstrip("josh!delete "):
                        file.write(quote)
                file.truncate()
                unethiquotes = file.readlines()
            await msg.channel.send(f"Forgetting: \'{msg.content.lstrip('josh!delete ')}\'")
    
        if msg.content == 'josh!latest':
            await msg.channel.send(unethiquotes[-1])

keep_alive()
client.run(TOKEN)