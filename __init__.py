import os
import socket
import discord
import asyncio
from discord.ext import commands
from discoin import Discoin
from .config import get_config

config = get_config()

bot = commands.Bot(command_prefix=">", pm_help=False)

discoin = Discoin(discoin_token)

@bot.event
async def on_ready():
    print('Finished loading!')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

if __name__ == "__main__":
    bot.run(config.token)
