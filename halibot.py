import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
import asyncio
import os

class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("MyCog Init")
        
    @app_commands.command(name="test", description="amogus")
    async def testcommand(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("sus")

class HaliBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    async def setup_hook(self):
        await self.add_cog(MyCog(self))
        print("Setup Hook")
        
    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        print('------')
        await self.register_commands()

    async def on_message(self, message):
        if message.author.bot:
            return
        print(f'Message from {message.author}: {message.content}')
        # await self.process_commands(message)
        
    async def register_commands(self):
        # Get app commands for bot
        global_commands = await self.fetch_global_commands()
        # List of slash commands to register
        slash_commands = [
            {
                "name":"test",
                "description":"amogus"
            }
        ]
        
        # Register slash commands if not registered
        for command in slash_commands:
            if not any(c["name"] == command["name"] for c in global_commands):
                await self.application_command_create(**command)
        
load_dotenv(find_dotenv())
token = os.getenv("DISCORD_TOKEN1")
owner_id = os.getenv("OWNER_ID")
# os.environ["DISCORD_TOKEN"] = ""
# print(os.getenv("DISCORD_TOKEN"))
print(token)
print(owner_id)

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
client = SmashBot(owner_id = owner_id, command_prefix = "!", intents = intents)

# client.run("")
client.run(token)
