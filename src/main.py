import discord
from importlib import import_module
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

prefix ="!"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix):
        command = message.content.lstrip(prefix)
        args = command.split(" ")
        
        try:
            if len(args) == 1:
                command_handler = import_module(f"commands.{args[0]}", package=None)
                await command_handler.command(message)
                dm_channel = await message.author.create_dm()
                await dm_channel.send("Hello dumbass")
                
            
            else: 
                command_handler = import_module(f"commands.{args[0]}", package=None)
                await command_handler.command(message, *args[1:])
                
                
        except ImportError as e:
            print(f"Command {command} not found {e}")
            await message.channel.send(f"Command {command} not found dumbass.")

        

client.run('MTE2NTc1Mzg3NjIwNTU1NTg2NA.G3NIg9.1jXJk9Zb1wCGvQxe6T7NQZj5m1Sf-LpcvaWfDI')