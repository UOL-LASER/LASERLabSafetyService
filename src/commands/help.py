async def command(client, message, *args):
    await message.channel.send('''
**!labentry** *(Full name)* *(Student ID)*: 
Upon entry to the lab, please execute this command with the required arguments.
**!labexit**: 
Upon exit from the lab, please execute this command to stop the checkup process.
''')