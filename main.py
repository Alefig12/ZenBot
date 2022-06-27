import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import requests

print("Running")
load_dotenv()
DTOKEN = os.getenv('DISCORD_TOKEN')

# Bot Commands Prefix
bot = commands.Bot(command_prefix='+') 



@bot.command(name='zen')

async def zenQuote(ctx):
    quote = await getRandomQuote()
    img_path = await generateImage(quote)
    await ctx.send(file= discord.File(img_path))

    

async def generateImage(quote):
    color = await getRandomColor()
    payload = {'text':quote, 'background_color':color}
    r = requests.get('https://web-series-quotes-api.deta.dev/pic/custom', params=payload)
    with open('img.jpeg', 'wb') as f:
        f.write(r.content)
        img_path = 'img.jpeg'
    return img_path


async def getRandomColor():
    
    r = requests.get('https://web-series-quotes-api.deta.dev/colors')
    random_color = random.choice(r.json())
    return random_color

async def getRandomQuote():
    r = requests.get('https://zenquotes.io/api/random/')
    quote = r.json()[0]['q']
    return quote

bot.run(DTOKEN) 





