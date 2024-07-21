def setup_ready_event(bot):
    @bot.event()
    async def event_ready():
        print(f"Twitch bot {bot.nick} is ready!")
        # Add any additional setup logic here