import discord
import os
import asyncio
import random

### Music Bot ###
# import music

# cogs = [music]

# client = commands.Bot(command_prefix = '?', intents = discord.Intents.all())

# for i in range (len(cogs)):
#     cogs[i].setup(client)
    
######## Welcome Bot/ Goodbye Bot 

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    welcomechannel = await client.fetch_channel(909192549778989117)
    print('Welcome')
    print(client.user.name)
    print('-----------------')

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
    await welcomechannel.send(f"Goodbye {member.mention}. We are going to miss you 😥! \nCome back soon!")
    print(f'{member.name} left the server')


### Message bot 
# Author : Jessica and Mary Moor 
# The purpose of this code is to have the bot reply to a user when they write and send
# a specific frase like '$hello'. We call this the Message Bot
@client.event
async def on_message(message):
    if message.author == client.user:
        """
        This function will 
        """
        return

    if message.content.startswith('$hello'):
        """
        This function will recognize that the user has sent the
        key frase '$hello' and the bot will reply to the user with one of the
        following frases in the hello list below. This is randomized to get 
        a different outcome each time! 
        """
        hello_list = ["Hello friend!", "Hello! It's nice to see you.", "Hello! Hope you enjoy your day!"]
        await message.channel.send(random.choice(hello_list))

    if message.content.startswith('$bye'):
        """
        This function will recognize that the user has sent the
        key frase '$bye' and the bot will reply to the user with one of the
        following frases in the hello list below. This is randomized to get 
        a different outcome each time!  
        """
        bye_list = ["Goodbye friend!", "Goodbye. Hope to see you soon.", "Goodbye. Save travels."]
        await message.channel.send(random.choice(bye_list))

    if message.content.startswith("$version"):
        """
        This function is the version function. This will allow the user to display an 
        outlined box with the parameters set here, only when a user writes and sends 
        '$version' in the 'bot-tests' channel. This will tell the users what version 
        we are currently working off of, and who updated it. 
        """
        bot_test = client.get_channel(900825491961958430)

        myEmbed = discord.Embed(title = "Current Verson", description = "The bot is in Version 2.0",
         color = 0x00ff00)
        myEmbed.add_field(name = "Version Code: ", value = 'v2.0.0', inline = False)
        myEmbed.add_field(name = "Date Released: ", value = "November 23, 2021", inline = False)
        myEmbed.set_footer(text = "Version 1.0 done by Jess and Mary")
        myEmbed.set_author(name = "Version Update by: Jess and Mary")

        await bot_test.send(embed = myEmbed)

###Banned Word Bot

bad_words = ['apple']
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    message_split = message.content.split(".")

    for message_word in message_split:
        for bad_word in bad_words:
            if bad_word == message_word.lower():
                await message.delete()
                await message.channel.send("😨 I have deleted your message... it is banned! 😳" +
                "\nPlease don't do it again! 🙄")


client.run(os.getenv('TOKEN'))