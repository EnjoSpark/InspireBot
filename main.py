import os
import discord
import json
import requests
from dotenv import load_dotenv


load_dotenv()

intents = discord.Intents(messages=True, message_content=True)
client = discord.Client(intents=intents)

sad_words = ['sad', 'unhappy', 'angry', 'miserable', 'depress', 'hate']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('$inspire') or any(word in msg.content for word in sad_words):
        print(f'Inspired {msg.author.name}.')
        await msg.channel.send(get_quote())


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " --" + json_data[0]['a']
    return quote


client.run(os.environ['TOKEN'])
