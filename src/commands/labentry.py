from data import labuser as lu

async def command(message, *args):
    newlabuser = lu.LabUser(args[0], args[1], args[2])
    
    dm_channel = await message.author.create_dm()
    await dm_channel.send("Hello dumbass")

    
    