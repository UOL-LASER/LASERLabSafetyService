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
        await asyncio.create_task(whileinlab(client, message, newlabuser))
        
        
        

async def whileinlab(client, message, newlabuser):
    global running_processes
    id = message.author.id
    dm_channel = await message.author.create_dm()
    
    await dm_channel.send("You are now signed into the lab, please remember to verify your safety every hour. \nEnsure you run *!labexit* in the server when leaving.")
    while running_processes.get(id, True):
        await asyncio.sleep(1800)
        print(f"Running processes while running: {running_processes}")
        await dm_channel.send("Please verify your safety by replying to this message. \nFailure to do so in the next 10 minutes will result in an alert to check up on you.")
        
        try:
            await client.wait_for('message', message.author.id == id, timeout=600)
            await dm_channel.send("Safety verification complete.")
        except asyncio.TimeoutError:
            await dm_channel.send("No response received. Sending an alert for someone to check up on you.")
            await message.channel.send(f"@everyone \n**{newlabuser.name}** with Student ID: **{newlabuser.studentid}** signed into the lab at: **{newlabuser.labentrydatetime}**. \nHas failed to respond to a verification check 10 minutes ago, therefore a checkup may be necessary to ensure their well-being.")
            

            
            
        
        
        
    running_processes.pop(id, None)
    print(f"Running processes after loop ends: {running_processes}")



    
    