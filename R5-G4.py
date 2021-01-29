import random

import discord

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user}: Bwoooooop!".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$R5: Obligation'):
        await message.channel.send("*Whistle*: " + str(random.randint(1, 100)))

    if message.content.startswith('$R5-G4'):
        await message.channel.send("BEEEEeeeep!")


client.run()
