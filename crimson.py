from colorama import Fore, Style, init
from discord.ext.commands import Bot
import discord
from discord.ext import commands
from discord.ext import commands, tasks
from urllib.parse import urlencode
import urllib.parse, urllib.request, requests, aiohttp
import re
from random import randint
import json
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
import time
import json
from discord import Permissions
import praw
import colorama
from colorama import Fore, Style, init
from discord.ext.commands import Bot
from urllib.parse import urlencode
import urllib.parse, urllib.request, requests, aiohttp
from discord.utils import get
import string
import subprocess
import re
from discord_webhook import DiscordWebhook
from itertools import cycle

user_id = "USER ID"
bot = commands.Bot(command_prefix='!', bot=False)

#do !help for command info
 
print(f"""
{Fore.RED}    
 ██████╗        ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝        ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║     █████╗  ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║     ╚════╝  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚██████╗        ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚═════╝        ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                       
                               Version V1     
                            Made by Anti
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
@Red.command()
async def at(ctx, *, text): # 
   await ctx.message.delete()
   r = requests.get(f'http://patorjk.com/software/taag/#p=display&f=Graffiti&t={urllib.parse.quote_plus(text)}').text
   if len('```'+r+'```') > 2000:
       return
   await ctx.send(f"```{r}```")
@Red.command()
async def bb(ctx): # 
   await ctx.message.delete()
   await ctx.send('ﾠﾠ'+'\n' * 500 + 'ﾠﾠ')
@Red.command()
async def gs(ctx, *, message):
   await ctx.message.delete()
  while True:
    await ctx.send(message, delete_after = 0.5)
@Red.command()
async def s(ctx, *, message):
   await ctx.message.delete()
  while True:
    await ctx.send(message)                
@Red.command()
async def sa(ctx, *, message):
 await ctx.message.delete()
 guild = ctx.guild
 while True:
   for channel in guild.text_channels:
     try:
       await channel.send(message)
     except:
       pass
    
Red.run('token', bot=False)
