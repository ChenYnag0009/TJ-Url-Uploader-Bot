# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from database.access import techvj
from pyrogram.types import Message
from config import Config

LOG_TEXT_P = """#NewUser  
ID - <code>{}</code>  
Name - {}  
Username - @{}  
User Link - {}  
Forward Video - {}"""

async def AddUser(bot: Client, update: Message):
    if not await techvj.is_user_exist(update.from_user.id):
        await techvj.add_user(update.from_user.id)

        # Log info about the user with username and user link
        log_info = LOG_TEXT_P.format(
            update.from_user.id,
            update.from_user.first_name,
            update.from_user.username if update.from_user.username else "N/A",
            update.from_user.mention,
            "Yes" if update.video else "No"
        )
        log_info += "\nUsername: @" + (update.from_user.username if update.from_user.username else "")
        log_info += "\nUser Link: " + update.from_user.mention
        
        # Send log info to the log channel
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)

    # Check if video is received, then call ForwardVideoAndLog
    if update.video:
        await ForwardVideoAndLog(bot, update, video_file_id=update.video.file_id)
