from data.globals import running_processes

async def command(client, message, *args):
    global running_processes
    id = message.author.id
    
    if id in running_processes and running_processes.get(id, True):
        print(f"User ID: {message.author.id}")
        running_processes[id] = False

        await message.channel.send(f"{message.author.mention}\nYou are signed out from the lab.")
        return
    
    elif id not in running_processes:
        await message.channel.send(f"{message.author.mention}\nYou are not signed into the lab, please refer to *!help* on how to sign in.")
        return