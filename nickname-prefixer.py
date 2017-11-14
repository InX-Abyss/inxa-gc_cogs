import discord
from discord.ext import commands


class nickNamePrefixer:
    """Cog developed by: InXA-GC"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """Enables nickNamePrefixer functionality for the server."""

        # Functional code goes here.
        await self.bot.say("I'm not working yet! Check back later...")


def setup(bot):
    bot.add_cog(nickNamePrefixer(bot))
