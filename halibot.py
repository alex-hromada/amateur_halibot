import discord
import asyncio
from discord_bot.bot import DiscordBot
from twitch_bot.bot import TwitchBot
from utils.logger import main_logger
from config import DISCORD_TOKEN, DISCORD_BOT_OWNER, TWITCH_TOKEN, TWITCH_CLIENT_ID, TWITCH_CHANNEL

async def main():
    main_logger.info("Starting Halibot")
    discord_bot = DiscordBot()
    twitch_bot = TwitchBot()

    try:   
        await asyncio.gather(
            discord_bot.start(DISCORD_TOKEN),
            twitch_bot.start()
        )
    except Exception as e:
        main_logger.error(f"Error occurred: {str(e)}", exc_info=True)
        

if __name__ == "__main__":
    asyncio.run(main()) 
