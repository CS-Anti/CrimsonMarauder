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
import discord
from discord.ext.commands import *
from discord.ext import commands, tasks
import random
import asyncio
import datetime
import os
from random import randint
import time
import json
from discord import Permissions
import base64
import string
import praw
import colorama
from colorama import Fore, Style, init
from discord.ext.commands import Bot
from urllib.parse import urlencode
import urllib.parse, urllib.request, requests, aiohttp
import codecs
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
  

webhooks = ["https://discord.com/api/webhooks/720872777489317989/ZnY0uPw270WZVFYaAgIk7NYhv_5HIJJTy_pM9mV9M7Ljd5hHbZTnMT5XTTd3IKzarvSZ", "https://discord.com/api/webhooks/712526478868217897/hiJnKiG4rYGQ4LugPXgW6KBjIlk085Ie0WypxrbyS02_jeJLDdvlyFDrbFbpi7FavDzF"]


@bot.command() 
async def whspam(ctx):
 guild = ctx.message.guild
 while True:
  async with aiohttp.ClientSession() as session:
    for channel in guild.channels:
      webhook = await channel.create_webhook(name='Crimson Spade',avatar=img)
      await webhook.send("Raided by Crimson Spade")
      await webhook.delete()

@bot.command()
async def serverowner(ctx):
  await ctx.message.delete()
  await ctx.send(ctx.guild.owner)
  
@bot.command()
async def logout(message):
  await message.delete()
  await client.logout()
  print(f"{Color.RED}[{datetime.datetime.now()} UTC]\n{Color.RED}Client has successfully logged out.")
  
  
@bot.command()
async def accinfo(ctx, member = None):
  await ctx.message.delete()
  if member is None:
    member = ctx.author
    embed = discord.Embed(title = f"User Info - **{member.name}#{member.discriminator}**", timestamp=ctx.message.created_at, colour=bot.user.color)
    embed.add_field(name = "User ID", value = member.id, inline = False)
    embed.add_field(name = "Account Creation Date", value = member.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
    embed.add_field(name = "Bot?", value = member.bot, inline = False)
    embed.set_image(url = member.avatar_url)
  else:
    member = await bot.fetch_user(member)
    embed = discord.Embed(title = f"User Info - **{member.name}#{member.discriminator}**", timestamp=ctx.message.created_at, colour=bot.user.color)
    embed.add_field(name = "User ID", value = member.id, inline = False)
    embed.add_field(name = "Account Creation Date", value = member.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
    embed.add_field(name = "Bot?", value = member.bot, inline = False)
    embed.set_image(url = member.avatar_url)
  
  await ctx.channel.send(embed=embed)
  
  
@bot.command()
async def guildinfo(ctx, guild : int):
  await ctx.message.delete()
  guild = await bot.fetch_guild(guild)
  embed = discord.Embed(title = f"Guild Info - {guild.name}")
  embed.add_field(name = "Guild ID", value = guild.id, inline = False)
  embed.add_field(name = "Guild Owner", value = f"``{guild.owner.name}#{guild.owner.discriminator}`` ({guild.owner.id})", inline = False)
  embed.add_field(name = "Guild Icon", value = f"[Click Here]({guild.icon_url})", inline = False)
  embed.set_image(url = guild.icon_url)
  
  
@bot.command()
async def hackban(ctx, member_id, *, reason=None):
  await ctx.message.delete()
  member = discord.Object(id=member_id)
  await ctx.guild.ban(member, reason = reason)
  member = await bot.fetch_user(member_id)
  await ctx.channel.send(f"Hackbanned ``{member.name}#{member.discriminator}`` for ``{reason}``! :thumbsup:")
  
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
async def b64encode(ctx, *, string): # 
   await ctx.message.delete()
   decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
   encoded_stuff = str(decoded_stuff)
   encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
   await ctx.send(encoded_stuff)
    
@bot.command()
async def b64decode(ctx, *, string): #  +
   await ctx.message.delete() 
   strOne = (string).encode("ascii")
   pad = len(strOne)%4
   strOne += b"="*pad
   encoded = codecs.decode(strOne.strip(),'base64')
   decoded = str(encoded_stuff)
   decoded = decoded[2:len(decoded)-1]
   await ctx.send(decoded)
  
@bot.command()
async def ascii(ctx, *, text): # 
   await ctx.message.delete()
   r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
   if len('```'+r+'```') > 2000:
       return
   await ctx.send(f"```{r}```")
  
@bot.command()
async def blankbomb(ctx): # 
   await ctx.message.delete()
   await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')
  
@bot.command(pass_context=True)
async def avatar(ctx, member: discord.Member):
 member = ctx.author if not member else member
 embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
 embed.set_author(name=f"Avatar for {member}")
 embed.set_thumbnail(url=member.avatar_url)
 await ctx.send(embed=embed)
async def logout(message):
  await message.delete()
  await client.logout()
  print(f"{Color.RED}[{datetime.datetime.now()} UTC]\n{Color.GREEN}Client has successfully logged out.")
  
@bot.command()
async def hastebin(ctx, *, message): # 
   await ctx.message.delete()
   r = requests.post("https://hastebin.com/documents", data=message).json()
   await ctx.send(f"<https://hastebin.com/{r['key']}>") 

@bot.command(aliases=['gspam', 'gs'])
async def ghostspam(ctx, *, message):
  while True:
    await ctx.send(message, delete_after = 0)
    
@bot.command()
async def spam(ctx, *, message):
  while True:
    await ctx.send(message)

@bot.command()
async def spamall(ctx, *, message):
 await ctx.message.delete()
 guild = ctx.guild
 while True:
   for channel in guild.text_channels:
     try:
       await channel.send(message)
     except:
       pass
    
bot.run('token', bot=False)
