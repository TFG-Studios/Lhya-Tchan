import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True  # Required for member-related events
intents.message_content = True  # Enables the message content intent

client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("Bot Ready To Use!")
    print("-----------------")


@client.command()
async def hello(ctx):
    await ctx.send("مرحبا بعضو طاقمي المذهل ! رارارارارارا! ")


keep_alive()
client.run("MTMxOTM4ODk0NzAyMTA0MTc1NQ.GRs8tK.obUwm5z9Fdz3yjYgRdF0LCuti0zOUKfA5MYLuM")
