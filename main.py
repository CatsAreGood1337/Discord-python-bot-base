import requests, discord
from discord.ext import commands
from config import settings
from discord.utils import get

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
	print("bot setup")

#@bot.command()
#async def hello(ctx):
    #author = ctx.message.author
    #await ctx.send(f'Hello, {author.mention}!')

bot.run(settings['token'])