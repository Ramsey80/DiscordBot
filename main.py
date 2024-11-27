# Import the libraries so code works
# pip install discord.py
import discord
from discord.ext import commands
import os
import random
# pip install python-dotenv
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

# Imports the environment variables
load_dotenv("token.env")
# Creates a discord client to send a request to the discord API
client = discord.Client()
# Pulling our token from the token.env file for discord bot
token = os.getenv('TOKEN')

# Declaring intents for messages
intents = discord.Intents.all()
intents.message_content = True  # Make sure the bot has the proper permissions
client = discord.Client(intents=intents)

                      
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
        elif user_message.lower() == "region":
            await message.channel.send(f'Your EC2 region is {ec2_metadata.region}')
            return
        elif user_message.lower() == "ip":
            await message.channel.send(f'Your public ip is {ec2_metadata.public_ipv4}')
            return
        elif user_message.lower() == "zone":
            await message.channel.send(f'Your availbility zone is {ec2_metadata.availability_zone}')
            return
        elif user_message.lower() == "tell me about my server":
            await message.channel.send(f'Your EC2 region is {ec2_metadata.region}, Your public ip is {ec2_metadata.public_ipv4}, Your availbility zone is {ec2_metadata.availability_zone} ')
            return
# End Bot Responses


#Test code
client.run(token)
