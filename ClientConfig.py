import traceback
import os
import re


import discord
from discord.ext import commands

class SodaBotClassic(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        for cog in EXTENSIONS:
            try:
                await self.load_extension(f"{cog}")
            except commands.errors.ExtensionError:
                traceback.print_exc()

        await bot.load_extension("jishaku")


async def get_prefix(client, message):
    extras = ["Soda*", "So*", "sb!", "sb*"]
    comp = re.compile("^(" + "|".join(map(re.escape, extras)) + ").*", flags=re.I)
    match = comp.match(message.content)
    if match is not None:
        extras.append(match.group(1))
    return commands.when_mentioned_or(*extras)(client, message)


bot = SodaBotClassic(command_prefix=(get_prefix), intents=discord.Intents.all())

