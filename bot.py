import discord
from SqlTester import * 
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('online')

@client.command()
async def set(ctx, *, days):
    setID(client.user.id, days.lower())
    await ctx.send('set ' + DayGetter(str(client.user.id)))

@client.command()
async def delete(ctx, member : discord.Member):
    Delete(str(member.id))
    await ctx.send('Deleted user <@' + str(member.id) + '>')

@client.command()
async def get(ctx, member : discord.Member):
    await ctx.send(printID(str(member.id)))

client.run('NjYyNTIyODA1MTIzOTQwMzUz.Xg7OIw.XlS9zOTPk8ghdKmEiCIZePsKocU')
