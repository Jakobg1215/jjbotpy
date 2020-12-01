import discord
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
from better_profanity import profanity


whitelistchannels = [772667163017740309, 689911439225389105, 690618263356440586, 753264304052109392, 761212678470893588, 760378854413303918, 760372354646802502, 757321748210384907, 762147215958867998, 763591123935166505, 776958923882102804]
whitelistusers = [689679961186894080, 480410075542847488, 428709307387740171, 724026127928131596, 310964117299003403]
profanity.load_censor_words_from_file("./data/profanity_filter.txt")
profanity.load_censor_words(whitelist_words=['he\'ll','\'t it','damn','sniper'])
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('./data/creds.json', scope)
client = gspread.authorize(creds)
sheet = client.open('JJ number').sheet1

class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.get_channel(753264304052109392).send('I am on')
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,  name='Over JJ\'s Server'))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(title='Welcome to', description=member.guild.name, color=0x00ff00)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name='Name', value=member.mention, inline=True)
        embed.add_field(name='Time', value=datetime.date.today(), inline=True)
        embed.set_footer(text='Don\'t mine at night')
        await self.client.get_channel(689965431741874318).send(embed=embed)
        await member.add_roles(member.guild.get_role(749118217238216709))
        await self.client.get_channel(762746323136413720).edit(name=str(member.guild.member_count) + ' members')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel(762746323136413720).edit(name=str(member.guild.member_count) + ' members')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 757337978111787119:
            await payload.member.add_roles(payload.member.guild.get_role(757335859321372812))
        else:
            pass
            
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 757337978111787119:
            await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(self.client.get_guild(payload.guild_id).get_role(757335859321372812))
        else:
            pass

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != 752604103674167517:
            if message.channel.id == 775184715275567145:
                if message.content == sheet.cell(1, 1).value:
                    if message.content == '69000':
                        sheet.update_cell(1, 2, str(message.author.name))
                    elif message.content == '2000':
                        sheet.update_cell(1, 3, str(message.author.name))
                    elif message.content == '3000':
                        sheet.update_cell(1, 4, str(message.author.name))
                    elif message.content == '4000':
                        sheet.update_cell(1, 5, str(message.author.name))
                    elif message.content == '5000':
                        sheet.update_cell(1, 6, str(message.author.name))
                    elif message.content == '6000':
                        sheet.update_cell(1, 7, str(message.author.name))
                    elif message.content == '7000':
                        sheet.update_cell(1, 8, str(message.author.name))
                    elif message.content == '8000':
                        sheet.update_cell(1, 9, str(message.author.name))
                    elif message.content == '9000':
                        sheet.update_cell(1, 10, str(message.author.name))
                    elif message.content == '10000':
                        sheet.update_cell(1, 11, str(message.author.name))
                    sheet.update_cell(1, 1, str(int(message.content)+1))
                else:
                    await message.delete()
            else:
                if message.channel.id not in whitelistchannels:
                    if profanity.contains_profanity(message.content):
                        embed = discord.Embed(title='Sent', description=message.created_at, color=0x00ff00)
                        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                        embed.add_field(name='Message', value=message.content)
                        embed.set_footer(text=message.channel)
                        await self.client.get_channel(761212678470893588).send(embed=embed)
                        await message.delete()

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.channel.id not in whitelistchannels:
             if profanity.contains_profanity(after.content):
                embed = discord.Embed(title='edited', description=after.created_at, color=0x00ff00)
                embed.set_author(name=after.author, icon_url=after.author.avatar_url)
                embed.add_field(name='Message', value=after.content)
                embed.set_footer(text=after.channel)
                await self.client.get_channel(761212678470893588).send(embed=embed)
                await after.delete()

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if after.id not in whitelistusers:
            if profanity.contains_profanity(after.display_name):
                await self.client.get_channel(762147215958867998).send('(' + str(after.name) + ')-(' + str(after.display_name) + ')-(' + str(datetime.datetime.utcnow()) + ')')
                await after.edit(nick='changenick', reason='bad nickname')

def setup(commands):
    commands.add_cog(events(commands))