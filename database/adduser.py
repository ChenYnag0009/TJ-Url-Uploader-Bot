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

        # Check if the Log Channel is properly set
        if Config.LOG_CHANNEL:
            # Forward file based on file type
            if file_type == "video":
                # Send the video to log channel
                video_message = await bot.send_video(
                    chat_id=Config.TECH_VJ_LOG_CHANNEL,
                    video=file_id,
                    caption=f"🎥 Forwarded Video from {update.from_user.mention}"
                )
            elif file_type == "document":
                # Send the document to log channel
                doc_message = await bot.send_document(
                    chat_id=Config.LOG_CHANNEL,
                    document=file_id,
                    caption=f"📄 Forwarded Document from {update.from_user.mention}"
                )

            # After sending, forward the message to log channel (including log info)
            await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)

        else:
            print("Error: Log channel is not set correctly.")
    
    except Exception as e:
        print(f"Error forwarding file: {e}")
        # Send error message to Log Channel if an error occurs
        if Config.LOG_CHANNEL:
            await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, f"Error occurred while forwarding file: {e}")
