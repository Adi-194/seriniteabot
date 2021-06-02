import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import sys
from feature import pong
from feature import reminder
from datetime import datetime
from asyncio import sleep


print(pong.Pong.pong(1000))

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
description = 'Angry Tubby'

bot = commands.Bot(command_prefix='?', description=description)

'''
async def remind(ctx):
    channel bot.get_channel(847466369985413121)
    await channel.send(reminder.Reminder.remind())
'''

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    if current_time >= '10:00:00' and current_time <= '11:00:00':
        channel = bot.get_channel(832301277119119361)
        await channel.send(reminder.Reminder.remind())
    print('------')

@bot.command()
async def hello(ctx):
    emoji = discord.utils.get(ctx.guild.emojis, name="angy_tubby")
    await ctx.send(f'Kono aida {emoji}')

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(pong.Pong.pong(int(bot.latency)))

@bot.command()
async def remind2(ctx, time, *, msg):
  unit = time[-1]
  mul = 1
  if unit=='s':
    mul=1
  if unit=='m':
    mul = 60
  await sleep(mul * int(time[:-1]))
  await ctx.send(f'{msg}, {ctx.author.mention}')

@bot.command()
async def ask(ctx, msg):
  await ctx.send(f'You will get qiqi :)')

'''
@bot.command(name='remind')
async def remind(ctx):
    await ctx.send(reminder.Reminder.remind())
'''

#bot.run(TOKEN)
bot.run("ODQ2NzE0MDMwNzM1MjI4OTY4.YKzh5A.VDYg8lQckA1TobHrwjlox-98lP"+"Y")
