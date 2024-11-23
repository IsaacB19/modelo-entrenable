import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot=commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print(f'te has logeado como {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="./labels.txt", image_path = f"./{attachment.filename}"))
    else:
        await ctx.send("ups, no has cargado ninguna imagen")

bot.run("MTI1MTMzMzc1MzIxMzY4NTc2MQ.GBgxkt.1OldcK-OqVsi1cGQTqYsNqpqToOMGJyqlXmjbE")