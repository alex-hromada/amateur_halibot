from twitchio.ext import commands
from config import TWITCH_TOKEN, TWITCH_CLIENT_ID, TWITCH_CHANNEL
from .commands.general import setup_general_commands
# from .commands.moderation import setup_moderation_commands
from .events.ready import setup_ready_event

class TwitchBot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN,
            client_id=TWITCH_CLIENT_ID,
            nick="Halibot",
            prefix="!",
            initial_channels=[TWITCH_CHANNEL]
        )
        setup_general_commands(self)
        # setup_moderation_commands(self)
        setup_ready_event(self)