<<<<<<< HEAD
import discord
import datetime
from SqlTester import * 
from Workouts import *
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '!z ', )
client.remove_command('help')
days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

@client.event
async def on_ready():
    print('online')
    #UpdateWeek.start()

@client.command()
async def set(ctx, *, days = days[datetime.datetime.today().weekday()]):
    setID(str(ctx.message.author.display_name), str(ctx.message.author.id), days.lower())
    await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

@client.command()
async def delete(ctx, member : discord.Member):
    Delete(str(member.id))
    await ctx.send('Deleted user <@' + str(member.id) + '>')

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
async def listW(ctx):
    await ctx.send(ListW())

@client.command()
async def printW(ctx, num = 0):
    await ctx.send(PrintW(num))
    
@client.command()
async def addW(ctx):
    await ctx.send("Dm Angular to add your own workout")

@client.command()
async def help(ctx):
    embed1 = discord.Embed(color = discord.Color.orange())
    embed2 = discord.Embed(color = discord.Color.orange())

    embed1.set_author(name='Help Workout Tracker')
    embed1.add_field(name = '!z set <days>', value='Set your days of the week. Follow the command by the days of the week that you want to work out', inline=False)
    embed1.add_field(name = '!z get <user>', value='@ someone to get their days of the week', inline = False)
    embed1.add_field(name = '!z checkin <days> | !z checkin', value='Put this command followed by any amount of days to represent the days you worked out. Default value is today', inline = False)
    embed1.add_field(name = '!z checkout <days> | !z checkout', value='This command is to undo the days you worked out if you didn\'t actually go or made a mistake. Put this command followed by any amount of days to undo the days that you worked out. Default value is today', inline = False)
    embed1.add_field(name = '!z delete', value='Delete all of your info', inline = False)

    embed2.set_author(name='Help Program List')
    embed2.add_field(name = '!z listW', value='Show the list of current workouts', inline=False)
    embed2.add_field(name = '!z printW <id>', value='Show a specific workout', inline=False)
    embed2.add_field(name = '!z addW', value='Add your own program. Temporarily tells you to DM Angular', inline=False)


    await ctx.author.send(embed = embed1)
    await ctx.author.send(embed = embed2)
    await ctx.send('Check out your dm\'s for command help!')
client.run('NjY0NzE0MjA0MTQ1NjQ3NjE2.XhdRmg.ReygtvYVEMk-iK0lcOLjk7LW1bc')



#@client.command()
#async def add(ctx, *, days = days[datetime.datetime.today().weekday()]):
#    Add(ctx.message.author.id, True, days.lower())
#    await ctx.send('Nice, let\'s do it')
#    await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

#@client.command()
#async def remove(ctx, *, days = days[datetime.datetime.today().weekday()]):
#    Add(ctx.message.author.id, False, days.lower())
#    await ctx.send('Maybe too much for little babies')
    #await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

#@tasks.loop(minutes = 45)
#async def UpdateWeek():
#    if(int(datetime.datetime.today().weekday()) == 1 and int(datetime.datetime.now().time().hour) == 1):
#        NewDay()
=======
import discord
import datetime
from SqlTester import * 
from Workouts import *
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '!z ', )
days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']

@client.event
async def on_ready():
    print('online')
    #UpdateWeek.start()

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
async def listW(ctx):
    await ctx.send(ListW())

@client.command()
async def printW(ctx, num = 0):
    await ctx.send(PrintW(num))
    
@client.command()
async def addW(ctx):
    await ctx.send("Dm Angular to add your own workout")
#@client.command()
#async def add(ctx, *, days = days[datetime.datetime.today().weekday()]):
#    Add(ctx.message.author.id, True, days.lower())
#    await ctx.send('Nice, let\'s do it')
#    await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

#@client.command()
#async def remove(ctx, *, days = days[datetime.datetime.today().weekday()]):
#    Add(ctx.message.author.id, False, days.lower())
#    await ctx.send('Maybe too much for little babies')
    #await ctx.send('Workout Days: ' + DayGetter(str(ctx.message.author.id)))

#@tasks.loop(minutes = 45)
#async def UpdateWeek():
#    if(int(datetime.datetime.today().weekday()) == 1 and int(datetime.datetime.now().time().hour) == 1):
#        NewDay()


>>>>>>> 9a021e80eb8d8dd12a37a0d1e625e01deafe039b
