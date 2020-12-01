import discord
import datetime
from discord.ext import commands

class modcommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help='Bans a member', description='Bans the member that you give')
    @commands.has_role('Staff')
    async def ban(self, ctx, member: discord.Member, deletmsg=1, *, reason=None):
        await ctx.guild.ban(user=member, delete_message_days=deletmsg, reason=reason)

    @commands.command(help='warns a member', description='Warns the member that you give')
    @commands.has_role('Staff')
    async def warn(self, ctx, member: discord.Member):
        await ctx.message.delete()
        if not ctx.guild.get_role(758445227102044220) in member.roles:
            await member.add_roles(ctx.guild.get_role(758445227102044220))
            await ctx.send(str(member.mention) + ' was warned by ' + str(ctx.author.mention))
        elif not ctx.guild.get_role(758445332828389467) in member.roles:
            await member.add_roles(ctx.guild.get_role(758445332828389467))
            await ctx.send(str(member.mention) + ' was warned by ' + str(ctx.author.mention))
        elif not ctx.guild.get_role(758445396032356382) in member.roles:
            await member.add_roles(ctx.guild.get_role(758445396032356382))
            await ctx.send(str(member.mention) + ' was warned by ' + str(ctx.author.mention))
        else:
            await ctx.send(str(member.mention) + ' has been warned 3 times!')

    @commands.command(help='mutes a member', description='Mutes the member that you give')
    @commands.has_role('Staff')
    async def mute(self, ctx, member: discord.Member):
        await ctx.message.delete()
        if not ctx.guild.get_role(761086719042519052) in member.roles:
            await member.add_roles(ctx.guild.get_role(761086719042519052))
            await ctx.send(str(member.mention) +  ' was muted by ' + str(ctx.author.mention))
        else:
            await ctx.send(str(member.mention) + ' is already muted!')

    @commands.command(help='unmutes a member', description='Unmutes the member that you give')
    @commands.has_role('Staff')
    async def unmute(self, ctx, member: discord.Member):
        await ctx.message.delete()
        if ctx.guild.get_role(761086719042519052) in member.roles:
           await member.remove_roles(ctx.guild.get_role(761086719042519052))
           await ctx.send(str(member.mention) + ' was unmuted by ' + str(ctx.author.mention))
        else:
            await ctx.send(str(ctx.author.mention) + ' is not muted!')

    @commands.command(hidden=True, description='Pings people that jj is live')
    @commands.has_role('Staff')
    async def islive(self, ctx, game=None, message=None, time=None, footnote=None):
        await self.client.get_channel(690713527798857769).send(ctx.guild.get_role(757335859321372812).mention)
        embed = discord.Embed(title='Stream Link', url='https://www.twitch.tv/jjpokey', description='Stream info', color=0x00ff00)
        embed.set_author(name=ctx.author, url=ctx.author.avatar_url, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/690618263356440586/750055318788112495/profile_picture.jpg')
        embed.add_field(name='Game', value=game, inline=True)
        embed.add_field(name='Message', value=message, inline=True)
        embed.add_field(name='Starting in', value=time, inline=True)
        embed.set_footer(text=footnote)
        await self.client.get_channel(690713527798857769).send(embed=embed)

    @commands.command(help='clears the chat', description='clears the channel of messages that you put')
    @commands.has_role('Staff')
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=(amount+1))

    @commands.command(hidden=True, description='Command can only work with owner')
    @commands.is_owner()
    async def test(self, ctx):
        pass

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you got to select a member!') 
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you can\'t ban this member!')
        elif isinstance(error, commands.MissingRole):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you don\'t have the permissons to do that!')

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you got to select a member!') 
        elif isinstance(error, commands.MissingRole):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you don\'t have the permissons to do that!')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you got to select a member!') 
        elif isinstance(error, commands.MissingRole):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you don\'t have the permissons to do that!')

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you got to select a member!') 
        elif isinstance(error, commands.MissingRole):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you don\'t have the permissons to do that!')

    @islive.error
    async def islive_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you don\'t have the permissons to do that!')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.message.delete()
            await ctx.send(str(ctx.author.mention) + ' you don\'t have the permissons to do that!')

def setup(commands):
    commands.add_cog(modcommands(commands))