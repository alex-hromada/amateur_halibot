def setup_ready_event(bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name} ({bot.user.id})')
        print('------')
        await bot.register_commands()
        print("Commands registered!")
        # Add any additional setup logic here