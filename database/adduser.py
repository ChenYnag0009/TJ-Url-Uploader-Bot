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

async def ForwardVideoAndLog(bot: Client, update: Message, video_file_id: str):
    try:
        # Prepare log information including username and user link
        log_info = f"Video forwarded from {update.from_user.first_name} (@{update.from_user.username})"
        log_info += f"\nUsername: @{update.from_user.username if update.from_user.username else 'N/A'}"
        log_info += f"\nUser Link: {update.from_user.mention}"

        # Forward video to the Log Channel
        video_message = await bot.send_video(
            chat_id=Config.TECH_VJ_LOG_CHANNEL,
            video=video_file_id,
            caption=f"🎥 Forwarded Video from {update.from_user.mention}"
        )
        
        # Log the sender's information to the channel
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)

    except Exception as e:
        print(f"Error forwarding video: {e}")
        # Optional: Send a message to Log Channel if error occurs
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, f"Error occurred while forwarding video: {e}")
