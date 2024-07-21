import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv(),
            verbose=True,
            override=True)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_BOT_OWNER = os.getenv("OWNER_ID")
TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")

print(TWITCH_CHANNEL)