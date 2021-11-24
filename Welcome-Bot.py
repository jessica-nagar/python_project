import discord
import os
import asyncio

######## Welcome bot 

intents = discord.Intents(members = True)
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    welcomechannel = await client.fetch_channel(909192549778989117)
    print('Welcome')
    print(client.user.name)
    print('-----')

@client.event
async def on_member_join(member):
    print("Recognised that a member " + member.name + " joined")
    welcomechannel = await client.fetch_channel(909192549778989117)
    await welcomechannel.send(f"Welcome {member.mention}!")
    print(f'{member.name} joined the server')

@client.event
async def on_disconnect():
    welcomechannel = await client.fetch_channel(909192549778989117)
    print('Welcome')
    print(client.user.name)
    print('-----')

@client.event
async def on_member_remove(member):
    print("Recognised that a member called " + member.name + " left")
    welcomechannel = await client.fetch_channel(909192549778989117)
    await welcomechannel.send(f"Goodbye {member.mention}!")
    print(f'{member.name} left the server')


client.run(os.getenv('TOKEN'))