import discord
import datetime
from SqlTester import * 
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '!')
days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

@client.event
async def on_ready():
    print('online')
    UpdateWeek.start()

@client.command()
async def set(ctx, *, days = days[datetime.datetime.today().weekday()]):
    setID(str(ctx.message.author.display_name), str(ctx.message.author.id), days.lower())
    await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

@client.command()
async def delete(ctx, member : discord.Member):
    Delete(str(member.id))
    await ctx.send('Deleted user <@' + str(member.id) + '>')

@client.command()
async def getO(ctx, member : discord.Member):
    #await ctx.send(printID(str(member.id)))
    await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))
    await ctx.send('Days Worked Out: ' + DayGetter(str(ctx.message.author.id), False))

@client.command()
async def get(ctx, member : discord.Member):
    await ctx.send(printID(str(member.id)))

@client.command()
async def printAll(ctx):
    await ctx.send(printall())

@client.command()
async def checkin(ctx, *, days = days[datetime.datetime.today().weekday()]):
    CheckIn(ctx.message.author.id, True, days.lower())
    await ctx.send('Good Job!')
    await ctx.send(printID(str(ctx.message.author.id)))

@client.command()
async def checkout(ctx, *, days = days[datetime.datetime.today().weekday()]):
    CheckIn(ctx.message.author.id, False, days.lower())
    await ctx.send('Unlucky')
    await ctx.send(printID(str(ctx.message.author.id)))

@client.command()
async def add(ctx, *, days = days[datetime.datetime.today().weekday()]):
    Add(ctx.message.author.id, True, days.lower())
    await ctx.send('Nice, let\'s do it')
    await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

@client.command()
async def remove(ctx, *, days = days[datetime.datetime.today().weekday()]):
    Add(ctx.message.author.id, False, days.lower())
    await ctx.send('Maybe too much for little babies')
    await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

@tasks.loop(minutes = 45)
async def UpdateWeek():
    if(int(datetime.datetime.today().weekday()) == 1 and int(datetime.datetime.now().time().hour) == 1):
        NewDay()

