import os
import re
import random
import discord
from discord.ext import commands
import subprocess

intents = discord.Intents.all()
intents.message_content = True

description = ''' '''
bot = commands.Bot(command_prefix='$', intents=intents)

script_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the script directory
resources_path = os.path.join(script_dir, 'resources')
reactions_path = os.path.join(script_dir, 'reactions')
summer_path = os.path.join(script_dir, '104', '104.mp4')

# List the contents of the directories
DUBSTEP = os.listdir(resources_path)
REACTIONS = os.listdir(reactions_path)

BACKUP_FILE = "leaderboard.txt"

number_sum = 0
user_message_counts=[]

if os.path.exists(BACKUP_FILE):
    with open(BACKUP_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) == 2:
                username = parts[0]
                try:
                    count = int(parts[1])
                except ValueError:
                    count = 0  
                user_message_counts.append([username, count])

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


def backup_data():
    """Writes the current user_message_counts list to the backup text file."""
    with open(BACKUP_FILE, "w") as file:
        for username, count in user_message_counts:
            file.write(f"{username}\t{count}\n")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="FIGMAXXING"))
    debugFunction()
    #uncomment for funny
    #bot.loop.create_task(send_message_loop())

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

@bot.command()
async def system_status(ctx):
    #change to read specific characters from neofetch as over 500 characters cannot be printed in one message 
    result = subprocess.run(['neofetch'], capture_output=True, text=True)
    await ctx.send(result)

@bot.command()
async def yapperboard(ctx):
    sorted_list = sorted(user_message_counts, key=lambda x: x[1], reverse=True)
    top_10 = sorted_list[:10]  # Get the top 10 entries

    # Build the response message
    response = "**Top 10 Yappers:**\n"
    for i, (username, count) in enumerate(top_10, start=1):
        response += f"{i}. {username} - {count} messages\n"

    await ctx.send(response)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.author == bot.user:
        return  # Prevent the bot from responding to its own messages
    
    username = message.author.name

    msg = message.content.lower()
    if 'sex' in msg or 'fruit' in msg or 'head' in msg or 'vegetable' in msg or 'csm' in msg:
        await message.channel.send(file=discord.File("resources/" + random.choice(DUBSTEP)))
        print("SEX DETECTED")
    
    if 'we are so back' in msg:
        rand_num = random.randint(0, 1)
        emoji = bot.get_emoji(1208655157982928896 if rand_num == 0 else 1208654541948583947)
        await message.add_reaction(emoji)

    #add apostrofy or 
    if 'its so joever' in msg:
        await message.channel.send(file=discord.File("reactions/sadsponge.mp4"))

    if 'blue drink' in msg:
        await message.channel.send(file=discord.File("reactions/bluedrink.mp4"))

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

    for user_data in user_message_counts:
        if user_data[0] == username:
            user_data[1] += 1  # Increment the message count
            break
    else:
        # If the user is not found, add a new entry with an initial count of 1.
        user_message_counts.append([username, 1])
    
    # Backup the updated list to the text file.
    backup_data()

    # Print the current state of the list for debugging purposes.
    print(user_message_counts)

    await bot.process_commands(message)

async def send_message_loop():
    await bot.wait_until_ready()  # Ensure the bot is ready before starting the loop
    channel_id = 1162197169328095243  # Replace with the actual channel ID
    channel = bot.get_channel(channel_id)
    
    if not channel:
        print("Channel not found")
        return
    
    while True:
        message = input("Enter a message to send to the Discord channel: ")
        await channel.send(message)
        print(f"Message sent: {message}")

FIGS = ["resources/fig1.jpg"]

FIG_STORY = "There is a specific species of wasps that lays their eggs inside of a fig called the Fig Wasp. When a Fig Wasp is ready to lay their eggs, they will crawl their way inside a fig, breaking all their legs just to fit inside the hole. The Fig Wasp will then lay their eggs inside a FEMALE Fig. When this happens, the fig will release enzymes to eat the wasp."

bot.run('MTE4NjUyODMwMTIzMDA2Mzc4Ng.GK40NG.BPgCM_FRXoNr4Qn6V_ZNrNdmsj6-xqs-MX1KGc')