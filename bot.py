#!/usr/bin/python3
import os
import discord
TOKEN=open("token.txt","r").readlines()[0]
ADMIN_ROLE="chleba"
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(
        f'{client.user} is connected to the following guild:\n'
    )
@client.event
async def on_message(message):

    print(message.content)
    for i in message.author.roles:
        if(i.name==ADMIN_ROLE):
            pass
client.run(TOKEN)
