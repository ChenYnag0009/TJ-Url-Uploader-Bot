# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from database.access import techvj
from pyrogram.types import Message
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message

LOG_TEXT_P = """#NewFile
ID - <code>{}</code>
Nᴀᴍᴇ - {}
Username: @{}
User Link: {}"""

async def DownloadAndForwardToLog(bot: Client, message: Message):
    # Download the file
    file_path = await message.download()

    # Prepare log information
    log_info = LOG_TEXT_P.format(
        message.from_user.id,
        message.from_user.first_name + (f" {message.from_user.last_name}" if message.from_user.last_name else ""),
        message.from_user.username if message.from_user.username else "N/A",
        message.from_user.mention
    )

    # Send the file to the log channel
    await bot.send_document(
        chat_id=Config.TECH_VJ_LOG_CHANNEL,
        document=file_path,
        caption=log_info
    )

# Handler for documents, videos, and photos
@bot.on_message(filters.document | filters.video | filters.photo)
async def handle_files(bot: Client, message: Message):
    await DownloadAndForwardToLog(bot, message)
