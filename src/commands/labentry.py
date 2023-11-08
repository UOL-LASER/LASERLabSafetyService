from data import labuser as lu
import datetime
import asyncio


            
async def command(client, message, *args):
    if len(args) < 3:
        await message.channel.send(f"{message.author.mention}\nNot enough arguments provided, please input your information to gain access to the lab.")
    else:
        newlabuser = lu.LabUser(f"{args[0]} {args[1]}", args[2], (datetime.datetime.now()))
        await asyncio.create_task(whileinlab(message, newlabuser))
        
async def whileinlab(message, newlabuser):
        dm_channel = await message.author.create_dm()
        while True:
            await dm_channel.send("Hello dumbass, you can't stop this hahahahaha")
            await asyncio.sleep(1)


    
    