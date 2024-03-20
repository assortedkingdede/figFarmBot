import os
import random
import discord
from discord.ext import commands
import DiscordUtils

intents = discord.Intents.all()
intents.message_content = True

description = ''' '''
bot = commands.Bot(command_prefix='$', intents=intents)

DUBSTEP = os.listdir('resources/')

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
    print('------')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="FIGMAXXING"))
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
async def fig_story(ctx):
    await ctx.send(FIG_STORY)

@bot.listen()
async def on_message(message):
    msg = message.content.lower()
    word = 'sex' # or could be a sentence or phrase (ie 'these words')
    if word in msg:
        await message.channel.send(file=discord.File("resources/" + DUBSTEP[random.randint(0, len(DUBSTEP) - 1)]))
        print("SEX DETECTED")

    if 'listener' in message.content.lower():
        #\:YourEmoji: in discord to get id 
        emoji = bot.get_emoji(1208654541948583947)
        await message.add_reaction(emoji)

    await bot.process_commands(message)

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

FIG_STORY = "There is a specific species of wasps that lays their eggs inside of a fig called the Fig Wasp. When a Fig Wasp is ready to lay their eggs, they will crawl their way inside a fig, breaking all their legs just to fit inside the hole. The Fig Wasp will then lay their eggs inside a FEMALE Fig. When this happens, the fig will release enzymes to eat the wasp."

bot.run('REDACTED')