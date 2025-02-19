# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from database.access import techvj
from pyrogram.types import Message
from config import Config

LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

 if Config.TECH_VJ_LOG_CHANNEL:
        try:
            log_message = await update.forward(Config.TECH_VJ_LOG_CHANNEL)
            log_info = "Message Sender Information\n"
            log_info += "\nFirst Name: " + update.from_user.first_name
            log_info += "\nUser ID: " + str(update.from_user.id)
            log_info += "\nUsername: @" + (update.from_user.username if update.from_user.username else "")
            log_info += "\nUser Link: " + update.from_user.mention
            await log_message.reply_text(
                text=log_info,
                disable_web_page_preview=True,
                quote=True
            )
