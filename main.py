import discord
from discord.ext import tasks, commands

# Replace with your bot token
TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.members = True  # Enable members intent
intents.guilds = True  # Enable guild intent

bot = commands.Bot(command_prefix='!', intents=intents)

# Counter to keep track of which status to display
status_counter = 0

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    update_status.start()  # Start the status update loop

@tasks.loop(seconds=10)  # Update status every 10 seconds
async def update_status():
    global status_counter

    # Get the total member count across all guilds the bot is in
    total_members = sum(guild.member_count for guild in bot.guilds)

    # Define the two custom statuses
    status_one = discord.CustomActivity(name=f"{total_members} members")  # Custom status with member count
    status_two = discord.CustomActivity(name="Playing with code!")  # Your other status

    # Rotate between the two statuses
    if status_counter % 2 == 0:
        await bot.change_presence(activity=status_one)
        print(f"Custom status updated to: {total_members} members")  # Log the status update
    else:
        await bot.change_presence(activity=status_two)
        print(f"Custom status updated to: Playing with code!")  # Log the other status

    # Increment the counter
    status_counter += 1

# Run the bot with your token
bot.run(TOKEN)
