import os
import socket
import discord
import asyncio
from discord.ext import commands
from discoin import Discoin




client = commands.Bot(command_prefix=">", pm_help=False)


discoin_token = "Censored"
discoin = Discoin(discoin_token)


@client.event
async def on_ready():
    print('Finished loading!')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == "__main__":
    bot.run("token")
