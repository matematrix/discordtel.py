import discord
from discord.ext import commands

class General:
    """General commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Ping-Pong command"""
        await ctx.send(embed=discord.Embed(title="Pong!",description="DiscordTel is online", color=discord.Color.blurple()))


def setup(bot):
    bot.add_extension(General(bot))
