import discord
from discord import app_commands
from discord.ext import commands
# from .commands import setup_commands
from .cogs.slash_commands import MyCog
from .events.ready import setup_ready_event

class DiscordBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        
    async def setup_hook(self):
        await self.add_cog(MyCog(self))
        setup_ready_event(self)
        print("Setup Hook")

    async def on_message(self, message):
        if message.author.bot:
            return
        print(f'Message from {message.author}: {message.content}')
        # await self.process_commands(message)
        
    # async def on_ready(self):
    #     print(f'Logged in as {self.user.name} ({self.user.id})')
    #     print('------')
    #     await self.register_commands()
    #     print("Commands registered!")
        
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
            
