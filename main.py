# Import the libraries so code works
# pip install discord.py
import discord
from discord.ext import commands
import os
import random
# pip install python-dotenv
from dotenv import load_dotenv

# Imports the environment variables
load_dotenv()
# Creates a discord client to send a request to the discord API
client = discord.Client()
# Pulling our token from the token.env file for discord bot
token = os.getenv('TOKEN')

# Declaring intents for messages
intents = discord.Intents.all()
intents.message_content = True  # Make sure the bot has the proper permissions
client = discord.Client(intents=intents)
# Declaring intents for commands
intents.members = True
bot = commands.Bot(command_prefix = ".", intents = intents)
                      
# Using on_ready to print the name of our bot
## Discord API command
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Start Bot Responses
@client.event
async def on_message(message):
    username = message.author
    channel = message.channel.name
    user_message = message.content
    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "random":
        if user_message.lower() == "hello" in ["hello", "hi"]:
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')
            return
        elif user_message.lower() == "tell me a joke":
            jokes = ["Can someone please shed more light on how my lamp got stolen?",
                     "Why is she called llene? She stands on equal legs.",
                     "What do you call a gazelle in a lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))
# End Bot Responses

# Allows the bot to listen to commands
bot = commands.Bot(command_prefix="!")
                      
# Creating a command
@bot.command(pass_context = True)
async def ping(ctx):
    await ctx.send("Pong!")

#Test code
client.run(token)
bot.run(token)