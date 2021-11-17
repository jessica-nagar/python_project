import discord
import os
import asyncio

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

######## Welcome bot 

intents = discord.Intents(members=True)
client=discord.Client(intents=intents)

@client.event
async def welcome_to():
    welcomechannel = await client.fetch_channel(909192549778989117)
    print('logged in as')
    print(client.user.name)
    print('-----')

newUserMessage = "Welcome to our server!"

@client.event
async def on_member_join(member):
    print("Recognised that a member " + member.name + " joined")
    try: 
        await client.send_message(member, newUserMessage)
        print("Sent message to " + member.name)
    except:
        print("Couldn't message " + member.name)
    embed=discord.Embed(
        title = "Welcome " + member.name + "!"
    )
        
 #   role = discord.utils.get(member.server.roles, name="name-of-your-role")
 #   await client.add_roles(member, role)
 #   print("Added role '" + role.name + "' to " + member.name)

@client.event
async def goodbye_fairwell(member):
    print("Recognised that a member " + member.name + " left")
    embed=discord.Embed(
        title="Goodbye "+member.name+"!",
    )

client.run(os.getenv('TOKEN'))