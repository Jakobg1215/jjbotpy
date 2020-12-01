import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix ='~', intents=discord.Intents.all(), description='Bot made by Jakobg1215#2245(428709307387740171)')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('REDACTED')