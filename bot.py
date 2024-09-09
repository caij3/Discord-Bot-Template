import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} has connected to Discord!')
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands.")

    @bot.tree.command(name="say", description="Repeats what you say.")
    async def say(interaction: discord.Interaction, message: str):
        await interaction.response.send_message(message)

    bot.run(TOKEN)

if __name__ == "__main__":
    run_bot()
