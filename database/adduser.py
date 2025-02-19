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

async def ForwardFileAndLog(bot: Client, update: Message, file_id: str, file_type: str):
    try:
        # Prepare log info for forwarding file
        log_info = f"File forwarded from {update.from_user.first_name} (@{update.from_user.username})"
        log_info += f"\nUsername: @{update.from_user.username if update.from_user.username else 'N/A'}"
        log_info += f"\nUser Link: {update.from_user.mention}"

        # Determine which file type is being sent
        if file_type == "video":
            await bot.send_video(
                chat_id=Config.TECH_VJ_LOG_CHANNEL,
                video=file_id,
                caption=f"🎥 Forwarded Video from {update.from_user.mention}"
            )
        elif file_type == "document":
            await bot.send_document(
                chat_id=Config.TECH_VJ_LOG_CHANNEL,
                document=file_id,
                caption=f"📄 Forwarded Document from {update.from_user.mention}"
            )

        # Send log info message to Log Channel
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)

    except Exception as e:
        print(f"Error forwarding file: {e}")
        # Send error message to Log Channel if an error occurs
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, f"Error occurred while forwarding file: {e}")
