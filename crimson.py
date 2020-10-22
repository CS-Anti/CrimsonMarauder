from colorama import Fore, Style, init
from discord.ext.commands import Bot
import discord
from discord.ext import commands
from discord.ext import commands, tasks
from urllib.parse import urlencode
import urllib.parse, urllib.request, requests, aiohttp
import re
from random import randint
from discord import Permissions
import requests
import random
import codecs
from itertools import cycle
from discord.utils import get
import string
import time
from colorama import Fore as color
from colorama import Fore as C, Style as S
import requests as req
import aiohttp
from threading import Thread as thr
from discord.ext.commands import *
from discord.ext import commands, tasks
import asyncio
import datetime
import os
from discord import Permissions
import praw
import colorama
from colorama import Fore, Style, init
from discord.ext.commands import Bot
from urllib.parse import urlencode
import urllib.parse, urllib.request, requests, aiohttp
from discord.utils import get
import string
from discord_webhook import DiscordWebhook
from itertools import cycle

user_id = "USER ID"
bot = commands.Bot(command_prefix='cm!', bot=False)

token = "token"

print(f"""
{Fore.RED}    
 ██████╗        ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝        ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║     █████╗  ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║     ╚════╝  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚██████╗        ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚═════╝        ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                       
                               Version V1     
                            Made by Herr Anti
                            {Fore.RED}
                            {Fore.RESET}
""")
@Red.command() 
async def whs(ctx):
 guild = ctx.message.guild
 while True:
  async with aiohttp.ClientSession() as session:
    for channel in guild.channels:
      webhook = await channel.create_webhook(name='Crimson Spade')
      await webhook.send("Raided by Crimson Spade")   
@Red.command()
async def serverowner(ctx):
  await ctx.message.delete()
  await ctx.send(ctx.guild.owner)  
@bot.command()
async def bb(ctx): 
   await ctx.message.delete()
   await ctx.send('ﾠﾠ'+'\n' * 500 + 'ﾠﾠ')
@bot.command()
async def gs(ctx, *, message):
   await ctx.message.delete()
  while True:
    await ctx.send(message, delete_after = 0.5)
@bot.command()
async def s(ctx, *, message):
   await ctx.message.delete()
  while True:
    await ctx.send(message)                
@bot.command()
async def sa(ctx, *, message):
 await ctx.message.delete()
 guild = ctx.guild
 while True:
   for channel in guild.text_channels:
     try:
       await channel.send(message)
     except:
       pass
@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        if msg.content == "cs":
            channel = msg.channel
            msg = await channel.history(limit=99999).flatten()
            for msg in msg:
                if msg.author == bot.user:
                    await msg.delete()
    
Red.run('token', bot=False)
