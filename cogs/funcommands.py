import discord
import random
from discord.ext import commands
from better_profanity import profanity

profanity.load_censor_words_from_file('./data/profanity_filter.txt')

class funcommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help='A random number', description='Gives you a random number between the numbers given')
    async def number(self, ctx, number1=0, number2=10):
        await ctx.send(round(random.uniform(number1, number2)))

    @commands.command(help='Bot says something', description='Makes the bot say what you put')
    async def say(self, ctx, *, message):
        if not profanity.contains_profanity(message):
            await ctx.send(message)
        else:
            await ctx.send(str(ctx.author.mention) + ' I can\'t say that!')

    @commands.command(help='Ping of the bot', description='Gives you the latency of the bot')
    async def ping(self, ctx):
        await ctx.send(str(round(self.client.latency*1000)) + 'ms')

    @commands.command(help='Info about the server', description='Gives info about this guild')
    async def serverinfo(self, ctx):
        embed=discord.Embed(title=ctx.guild.name, description='Server info', color=0x00ff00)
        embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name='emojis', value=len(ctx.guild.emojis), inline=True)
        embed.add_field(name='region', value=ctx.guild.region, inline=True)
        embed.add_field(name='afk', value=ctx.guild.afk_timeout, inline=True)
        embed.add_field(name='description', value=ctx.guild.description, inline=True)
        embed.add_field(name='verification_level', value=ctx.guild.verification_level, inline=True)
        embed.add_field(name='channels', value=len(ctx.guild.channels), inline=True)
        embed.add_field(name='categories', value=len(ctx.guild.categories), inline=True)
        embed.add_field(name='voice_channels', value=len(ctx.guild.voice_channels), inline=True)
        embed.add_field(name='text_channels', value=len(ctx.guild.text_channels), inline=True)
        embed.add_field(name='members', value=ctx.guild.member_count, inline=True)
        embed.add_field(name='roles', value=len(ctx.guild.roles), inline=True)
        embed.add_field(name='created_at', value=str(ctx.guild.created_at) + ' UTC', inline=True)
        embed.set_footer(text=str(ctx.guild.owner) + ' owns the server')
        await ctx.send(embed=embed)

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(str(ctx.author.mention) + ' you for got the message!')

def setup(commands):
    commands.add_cog(funcommands(commands))