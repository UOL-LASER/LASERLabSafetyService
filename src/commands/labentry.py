from data import labuser as lu
import datetime
import asyncio
from data.globals import running_processes

async def command(client, message, *args):
    global running_processes
    id = message.author.id

    if len(args) < 3:
        await message.channel.send(f"{message.author.mention}\nNot enough arguments provided, please input your information to gain access to the lab.")
    else:
        newlabuser = lu.LabUser(f"{args[0]} {args[1]}", args[2], (datetime.datetime.now()))
        running_processes[id] = True
        print(f"Running processes after set to True: {running_processes}")
        await message.channel.send(f"{message.author.mention}\nYou are signed into the lab.")
        await asyncio.create_task(whileinlab(message, newlabuser))
        
        
        

async def whileinlab(message, newlabuser):
    global running_processes
    id = message.author.id
    dm_channel = await message.author.create_dm()
    
    while running_processes.get(id, True):
        print(f"Running processes while running: {running_processes}")
        await dm_channel.send("Hello dumbass, you can't stop this hahahahaha")
        await asyncio.sleep(10)
    running_processes.pop(id, None)
    print(f"Running processes after loop ends: {running_processes}")



    
    