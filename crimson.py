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


tokens = open("tokens.txt", "r").read().splitlines()

user_id = "USER ID"
bot = commands.Bot(command_prefix='!', self_bot=True)


 
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
@bot.event
async def on_connect():
  print(f"""
  {Fore.RED}
  {Style.DIM}
  Logged in as: {bot.user.name} #{bot.user.discriminator}
  {Fore.RESET}
  """)

@bot.command() 
async def whspam(ctx):
 guild = ctx.message.guild
 while True:
  async with aiohttp.ClientSession() as session:
    for channel in guild.channels:
      webhook = await channel.create_webhook(name='Crimson Spade')
      await webhook.send("Raided by Crimson Spade")
      
@bot.command()
async def serverowner(ctx):
  await ctx.message.delete()
  await ctx.send(ctx.guild.owner)
  
  
@bot.command()
async def accinfo(ctx, member = None):
  await ctx.message.delete()
  if member is None:
    member = ctx.author
    embed = discord.Embed(title = f"Info - **{member.name}#{member.discriminator}**", timestamp=ctx.message.created_at, colour=bot.user.color)
    embed.add_field(name = "ID", value = member.id, inline = False)
    embed.add_field(name = "DOC", value = member.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
    embed.add_field(name = "Bot", value = member.bot, inline = False)
    embed.set_image(url = member.avatar_url)
  else:
    member = await bot.fetch_user(member)
    embed = discord.Embed(title = f"Info - **{member.name}#{member.discriminator}**", timestamp=ctx.message.created_at, colour=bot.user.color)
    embed.add_field(name = "ID", value = member.id, inline = False)
    embed.add_field(name = "DOC", value = member.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
    embed.add_field(name = "Bot", value = member.bot, inline = False)
    embed.set_image(url = member.avatar_url)
  
  await ctx.channel.send(embed=embed)
  
  
@bot.command()
async def gi(ctx, guild : int):
  await ctx.message.delete()
  guild = await bot.fetch_guild(guild)
  embed = discord.Embed(title = f"Guild Info - {guild.name}")
  embed.add_field(name = "Server Identification", value = guild.id, inline = False)
  embed.add_field(name = "Server Owner", value = f"``{guild.owner.name}#{guild.owner.discriminator}`` ({guild.owner.id})", inline = False)
  embed.add_field(name = "Server Avatar", value = f"[Click Here]({guild.icon_url})", inline = False)
  embed.set_image(url = guild.icon_url)
  
  
@bot.command()
async def pb(ctx, member_id, *, reason=None):
  await ctx.message.delete()
  member = discord.Object(id=member_id)
  await ctx.guild.ban(member, reason = reason)
  member = await bot.fetch_user(member_id)
  await ctx.channel.send(f"Prebanned ``{member.name}#{member.discriminator}`` for ``{reason}``! :sunglasses:")
  
@bot.command()
async def geolocate(ctx, *, ipaddr: str = '1.3.3.7'): # 
   await ctx.message.delete()
   r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
   geo = r.json()
   em = discord.Embed()
   fields = [
       {'name': 'IP', 'value': geo['query']},
       {'name': 'IP Type', 'value': geo['ipType']},
       {'name': 'Country', 'value': geo['country']},
       {'name': 'City', 'value': geo['city']},
       {'name': 'Continent', 'value': geo['continent']},
       {'name': 'IPName', 'value': geo['ipName']},
       {'name': 'ISP', 'value': geo['isp']},
       {'name': 'Latitute', 'value': geo['lat']},
       {'name': 'Longitude', 'value': geo['lon']},
       {'name': 'Region', 'value': geo['region']},
   ]
   for field in fields:
       if field['value']:
           em.add_field(name=field['name'], value=field['value'], inline=True)
   return await ctx.send(embed=em) 
 
@bot.command()
async def at(ctx, *, text): # 
   await ctx.message.delete()
   r = requests.get(f'http://patorjk.com/software/taag/#p=display&f=Graffiti&t={urllib.parse.quote_plus(text)}').text
   if len('```'+r+'```') > 2000:
       return
   await ctx.send(f"```{r}```")
 
@bot.command()
async def bb(ctx): # 
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
    
bot.run('token', bot=False)
