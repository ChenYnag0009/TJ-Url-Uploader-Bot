# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from database.access import techvj
from pyrogram.types import Message
from config import Config
from pyrogram import Client, Message
from pyrogram.types import InputMediaDocument

LOG_TEXT_P = """#NewFile
ID - <code>{}</code>
Nᴀᴍᴇ - {}
Username: @{}
User Link: {}"""

async def DownloadAndForwardToLog(bot: Client, update: Message):
    # Download the file
    file_path = await bot.download_media(update)
    
    # Prepare log information
    log_info = LOG_TEXT_P.format(
        update.from_user.id,
        update.from_user.first_name + (f" {update.from_user.last_name}" if update.from_user.last_name else ""),
        update.from_user.username if update.from_user.username else "N/A",
        update.from_user.mention
    )
    
    # Send the file to the log channel
    await bot.send_document(
        chat_id=Config.TECH_VJ_LOG_CHANNEL,
        document=file_path,
        caption=log_info
    )
