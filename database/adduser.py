# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from user_utils import AddUser  # Import the function from the file
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize your bot
bot = Client("bot.py")

# Example handler
@bot.on_message(filters.private)
async def handle_new_user(bot: Client, message: Message):
    await AddUser(bot, message)  # Call the AddUser function

# Start the bot
bot.run()
