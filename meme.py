import discord
import random
import time
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



@bot.command()
async def mem(ctx):
    with open(f'images/{random.choice(os.listdir("images"))}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def лох(ctx):
    with open(f'loose/{random.choice(os.listdir("loose"))}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'👆лох дня👆')
bot.run("MTE2MjY4MzQ3MjU3NDQzMTMzNg.GugWLN.iVkJJiuVy3XdFE4b2JmfVhOITC4zT9x-ydoLIY")