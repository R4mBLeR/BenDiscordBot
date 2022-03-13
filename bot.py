import discord
import random

client=discord.Client()
arr=["Yeees", "No", "Ho-ho-ho-ho"]

@client.event
async def on_message(message):
    if message.content.lower().startswith("бен"):
        await message.channel.send(random.choice(arr))

client.run("TOKEN")