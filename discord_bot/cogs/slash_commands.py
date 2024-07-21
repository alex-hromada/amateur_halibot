import discord
from discord.ext import commands
from discord import app_commands

class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("MyCog Init")
        
    @app_commands.command(name="test", description="amogus")
    async def testcommand(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("sus")

# class GeneralCog(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command()
#     async def ping(self, ctx):
#         await ctx.send("Pong!")