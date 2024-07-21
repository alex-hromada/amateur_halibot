def setup_general_commands(bot):
    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send(f"Pong! @{ctx.author.name}")

    # Add more general commands here