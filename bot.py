import os
import time
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

# Bot Modifier constant
ONE_TIME = False

# URL constants
url = "https://apod.nasa.gov/apod/astropix.html"
url_base = "https://apod.nasa.gov/apod/"


def get_img_url():
    # Soup init
    page = requests.get(url_base)
    soup = BeautifulSoup(page.content, "html.parser")

    # Get image url
    img_url = url_base + soup.find('img')['src']

    return img_url


def get_message_content():
    # Soup init
    page = requests.get(url_base)
    soup = BeautifulSoup(page.content, "html.parser")

    # Title of picture
    title = soup.find('b').text

    # Format message
    explanation = soup.find_all('p')[2]
    explanation = explanation.text.split("Tomorrow's picture")[0].strip()
    explanation = explanation.split("Explanation: ")[1].strip()
    temp = explanation.split('.')
    for i, s in zip(range(0, len(temp)), temp):
        temp[i] = s.replace('\n', ' ').replace('  ', ' ').strip()
    explanation = '.\n\n'.join(temp)

    return "**" + title + "**" + '\n\n' + explanation


# Connect to discord
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    send_message.start()

    if ONE_TIME:
        channel = client.get_channel(1065142615135227934)
        await channel.send(get_img_url())
        await channel.send(get_message_content())


@tasks.loop(hours=24.0)
async def send_message():
    channel = client.get_channel(1065142615135227934)
    await channel.send(get_img_url())
    await channel.send(get_message_content())

client.run(TOKEN)
