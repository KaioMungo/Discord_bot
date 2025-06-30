import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    syncs = await bot.tree.sync()
    print(f"{len(syncs)} comandos sincronizados!")
    print(f'Bot inicializado como {bot.user}')

    # Carregando cogs
    await bot.load_extension('cogs.eventos')
    await bot.load_extension('cogs.comandos')
    await bot.load_extension('cogs.tempo')

bot.run(os.getenv('SEU_BOT_TOKEN'))
