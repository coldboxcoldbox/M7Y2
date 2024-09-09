import os
import discord
from transliterate import translit, get_available_language_codes
from discord.ext import commands
from model import derevo

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description="ботяра", intents=intents)
@bot.command()
async def a(ctx):
    await ctx.send(f"Бот в сети")
@bot.command()
async def image_save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Изображение сохранено как ./{attachment.filename}")
            name = derevo(f"./{attachment.filename}")
            await ctx.send("Этот лист принадлежит дереву...")

            await ctx.send(translit(name, "ru"))
            link = "https://en.wikipedia.org/wiki/" + name
            await ctx.send("Статья на википедии:")
            await ctx.send(link)
    else:
        print("изображений не найдено")
bot.run("token")
