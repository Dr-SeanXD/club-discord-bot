import csv
import discord
from discord import app_commands
from discord.ext import commands
import pandas as pd


TOKEN = ''

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != 1299452290469593112:
        return

    emoji = str(payload.emoji)
    if emoji == "✅":
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = discord.utils.get(guild.roles, name="Member")
        await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != 1299452290469593112:
        return

    emoji = str(payload.emoji)
    if emoji == "✅":
        guild = bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        role = discord.utils.get(guild.roles, name="Member")
        await member.remove_roles(role)

@bot.event
async def on_ready():
    try:
        slash = await bot.tree.sync()
        print(f"Logged in as --> {bot.user}")
        print(f"Loaded {len(slash)} slash commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")

bot.run(TOKEN)