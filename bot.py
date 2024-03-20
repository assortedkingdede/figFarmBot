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
REACTIONS = os.listdir('resources/reactions/')

def debugFunction():
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

#not needed anymore
@bot.command()
async def hello(ctx):
    #helper function?
    await ctx.send("Who is Figging rn")
    print(ctx.message.author)

#depreciated remove?
@bot.command()
async def fig_me(ctx):
    await ctx.send(file=discord.File(FIGS[0]))
    print(ctx.message.author)

@bot.command()
async def fig_story(ctx):
    await ctx.send(FIG_STORY)

#Suggestion box feature
@bot.command()
async def suggestions(suggestion):
    #append to end of file instead of overwrite
    file = open("suggestionBox.txt", "a")
    file.write(suggestion.content.lower())
    file.close
    suggestion.send("Suggestion noted")

@bot.listen()
async def funnyResponse(message):
    msg = message.content.lower()
    #change word?
    word = 'sex' # or could be a sentence or phrase (ie 'these words')
    if word in msg:
        await message.channel.send(file=discord.File("resources/" + DUBSTEP[random.randint(0, len(DUBSTEP) - 1)]))
        print("SEX DETECTED")#, message.message.author#)

    if 'we are so back' in message.content.lower():
        #\:YourEmoji: in discord to get id 
        rand_num = random.randint(0, 1)
        if rand_num == 0:
            emoji = bot.get_emoji(1208655157982928896)
        if rand_num == 1:
            emoji = bot.get_emoji(1208654541948583947)
        
        await message.add_reaction(emoji)

    if 'its so joever' in message.content.lower():
        await message.channel.send(file=discord.File("resources/reactions/sadsponge.mp4"))

    await bot.process_commands(message)

FIGS = ["resources/fig1.jpg"]

FIG_STORY = "There is a specific species of wasps that lays their eggs inside of a fig called the Fig Wasp. When a Fig Wasp is ready to lay their eggs, they will crawl their way inside a fig, breaking all their legs just to fit inside the hole. The Fig Wasp will then lay their eggs inside a FEMALE Fig. When this happens, the fig will release enzymes to eat the wasp."

bot.run('REDACTED')