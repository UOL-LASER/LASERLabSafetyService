from modules.userhandler import UserHandling

async def command(message, args):
    args = args.split(" ")
    await UserHandling().start(args[0], args[1], message.author.id)