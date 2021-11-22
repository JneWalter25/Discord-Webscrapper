import discord
import asyncio
import os
from web import webscraper

penultimopost = webscraper.functionpublicacion()
TOKEN = os.environ['TOKEN']
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ultimopost'):
        await message.channel.send(webscraper.ultimapublicacion)


async def webfinal(penultimopost):
    await client.wait_until_ready()
    channel = client.get_channel(id=911283896656736256)
    while not client.is_closed():
        if penultimopost == webscraper.functionpublicacion():
            print(penultimopost)
            await asyncio.sleep(900)
        else:
            print(penultimopost)
            await channel.send(f"@everyone,{webscraper.functionpublicacion()}")
            penultimopost = webscraper.functionpublicacion()
            await asyncio.sleep(900)
client.loop.create_task(webfinal(penultimopost))

client.run(TOKEN)

