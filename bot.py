import random
import discord
from discord.ext import commands
import DiscordUtils

intents = discord.Intents.default()
intents.messages = True

description = ''' '''
bot = commands.Bot(command_prefix='$', intents=intents)

def debugFunction():
    print("debug function active")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for guild in bot.guilds:
        print(guild.name)
        print(guild.id)
        print(guild.owner)
        print(guild.member_count)
        print("DUBSTEP LIST LENGTH: ", len(DUBSTEP))
    print('------')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Currently Figging rn"))
    debugFunction()
    
@bot.command()
async def hello(ctx):
    #helper function?
    await ctx.send("Who is Figging rn")
    print(ctx.message.author)
    
@bot.command()
async def fig_me(ctx):
    await ctx.send(file=discord.File(FIGS[0]))
    print(ctx.message.author)

@bot.command()
async def dub_me(ctx):
    await ctx.send(file=discord.File(DUBSTEP[random.randint(0, len(DUBSTEP) - 1)]))
    print(ctx.message.author)

@bot.command()
async def fig_story(ctx):
    await ctx.send(FIG_STORY)

@bot.listen()
async def on_message(message):
    msg = message.content.lower()
    word = 'sex' # or could be a sentence or phrase (ie 'these words')
    if word in msg:
        await message.channel.send(file=discord.File(DUBSTEP[random.randint(0, len(DUBSTEP) - 1)]))
        print("SEX DETECTED")

@bot.event
async def help(ctx):
    await ctx.send("""Commands:
    !help: Shows this command
    !hello: Says World
    !add: Adds two numbers.
    !subtract: Subtracts one number from another.
    !multiply: Multiplys two numbers.
    !divide: Divides two numbers. """)

FIGS = ["resources/fig1.jpg"]

DUBSTEP = ["resources/figstep.mov", "resources/dragonstep.mov", "resources/grapestep.mov", "resources/cherrystep.mov", "resources/applestep.mov", "resources/watermelonstep.mov", "resources/orangestep.mov", "resources/bananastep.mov", "resources/lemonstep.mov", "resources/pumpkinstep.mov", "resources/figstep2.mov", "resources/appledit.mov", "resources/kiwistep.mov", "resources/leekstep.mov", "resources/blueberrystep.mov", "resources/coconut.mov", "resources/lychee.mov", "resources/beanstep.mov"]

FIG_STORY = "There is a specific species of wasps that lays their eggs inside of a fig called the Fig Wasp. When a Fig Wasp is ready to lay their eggs, they will crawl their way inside a fig, breaking all their legs just to fit inside the hole. The Fig Wasp will then lay their eggs inside a FEMALE Fig. When this happens, the fig will release enzymes to eat the wasp."

bot.run('REDACTED')