#there is a bug present where there is a chance of a directory within resources to be loaded as a file, restructure directories when possible

import os
import re
import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

description = ''' '''
bot = commands.Bot(command_prefix='$', intents=intents)

script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the script directory
resources_path = os.path.join(script_dir, 'resources')
reactions_path = os.path.join(resources_path, 'reactions')
summer_path = os.path.join(script_dir, '104', '104.mp4')

# List the contents of the directories
DUBSTEP = os.listdir(resources_path)
REACTIONS = os.listdir(reactions_path)

number_sum = 0

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

@bot.command()
async def hello(ctx):
    await ctx.send("Who is Figging rn")
    print(ctx.message.author)

@bot.command()
async def fig_me(ctx):
    await ctx.send(file=discord.File(FIGS[0]))
    print(ctx.message.author)

@bot.command()
async def fig_story(ctx):
    await ctx.send(FIG_STORY)

@bot.command()
async def suggestions(ctx, *, suggestion):
    with open("suggestionBox.txt", "a") as file:
        file.write(ctx.message.author.name + ': ' + suggestion.lower() + '\n')
    await ctx.send("Suggestion noted")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Prevent the bot from responding to its own messages

    msg = message.content.lower()
    if 'sex' in msg or 'fruit' in msg or 'head' in msg or 'vegetable' in msg or '21' in msg or 'oki' in msg or 'ok' in msg or 'csm' in msg:
        await message.channel.send(file=discord.File("resources/" + random.choice(DUBSTEP)))
        print("SEX DETECTED")
    
    if 'we are so back' in msg:
        rand_num = random.randint(0, 1)
        emoji = bot.get_emoji(1208655157982928896 if rand_num == 0 else 1208654541948583947)
        await message.add_reaction(emoji)

    if 'its so joever' in msg:
        await message.channel.send(file=discord.File("resources/reactions/sadsponge.mp4"))

    numbers_in_msg = re.findall(r'\d+', msg)
    numbers_in_msg = list(map(int, numbers_in_msg))

    global number_sum

    if numbers_in_msg:
        number_sum += sum(numbers_in_msg)  # Add the sum of numbers found in the message to the total
        print(f"Current sum of numbers: {number_sum}")

        # If the sum or individual number is 104, post the video
        if number_sum == 104:
            print('104 days of summer vacation')
            await message.channel.send(file=discord.File(summer_path))

        if number_sum > 104:
            print('Sum exceeded 104, resetting to zero')
            number_sum = 0

    await bot.process_commands(message)

FIGS = ["resources/fig1.jpg"]

FIG_STORY = "There is a specific species of wasps that lays their eggs inside of a fig called the Fig Wasp. When a Fig Wasp is ready to lay their eggs, they will crawl their way inside a fig, breaking all their legs just to fit inside the hole. The Fig Wasp will then lay their eggs inside a FEMALE Fig. When this happens, the fig will release enzymes to eat the wasp."

bot.run('INSERT')