import discord
import os
import asyncio

######## Welcome bot 

intents = discord.Intents(members = True)
client = discord.Client(intents = intents)

@client.event
async def welcome_to():
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
async def on_member_leave(member):
    print("Recognised that a member " + member.name + " left")
    welcomechannel = await client.fetch_channel(909192549778989117)
    await welcomechannel.send(f"Goodbye {member.mention}!")
    print(f'{member.name} left the server')

# @client.event
# async def on_member_leave(member): 
#     print("Recognised that a member " + member.name + " left")
#     welcomechannel = await client.fetch_channel(909192549778989117)
#     await welcomechannel.send(f"Goodbye {member.mention} we will miss you!")
#     print(f'{member.name} left the server')

    # try: 
    #     await client.send_message(member, newUserMessage)
    #     print("Sent message to " + member.name)
    # except:
    #     print("Couldn't message " + member.name)
    # embed =discord.Embed(
    #     title = "Welcome " + member.name + "!"
    # )
    
        
#    role = discord.utils.get(member.server.roles, name="name-of-your-role")
#    await client.add_roles(member, role)
#    print("Added role '" + role.name + "' to " + member.name)


client.run(os.getenv('TOKEN'))