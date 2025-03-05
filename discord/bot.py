import asyncio
import discord
from discord.ext import commands
from modules.helpers import *


client = commands.Bot(
    command_prefix=PREFIX,
    owner_ids=OWNER_IDS,
    intents=discord.Intents.all()
)

client.remove_command('help')


async def load_extensions():
    for filename in os.listdir(COG_FOLDER):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

asyncio.run(load_extensions())

client.run(TOKEN)
