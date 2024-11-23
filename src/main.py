import discord
from importlib import import_module
import os


token = os.getenv("DISCORD_SECRET")

if not token:
    print("Error: DISCORD_SECRET environment variable not found.")
    exit(1)

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
            command_handler = import_module(f"commands.{args[0]}", package=None) 
            await command_handler.command(client, message, *args[1:])
                
                
        except ImportError as e:
            print(f"Command {command} not found {e}")
            await message.channel.send(f"{message.author.mention}\nCommand *{command}* not found.")

        

client.run(token)