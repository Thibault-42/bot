# This example requires the 'message_content' intent.
import os
import discord
import smtplib
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["BOT_TOKEN"]
SMTP_USER = os.environ["SMTP_USER"]
EMAIL_TO = os.environ["EMAIL_TO"]

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(TOKEN)