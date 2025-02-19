# user_utils.py
from pyrogram import Client
from pyrogram.types import Message

LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}
Username: @{}
User Link: {}"""

async def AddUser(bot: Client, message: Message):
    if not await techvj.is_user_exist(message.from_user.id):
        await techvj.add_user(message.from_user.id)
        
        # Prepare log information
        log_info = LOG_TEXT_P.format(
            message.from_user.id,
            message.from_user.first_name + (f" {message.from_user.last_name}" if message.from_user.last_name else ""),
            message.from_user.username if message.from_user.username else "N/A",
            message.from_user.mention
        )
        
        # Send log message to the log channel
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)
