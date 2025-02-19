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

        log_info = LOG_TEXT_P.format(
            update.from_user.id,
            update.from_user.first_name,
            update.from_user.username if update.from_user.username else "N/A",
            update.from_user.mention,
            "Yes" if update.video else "No"  # Checking if the message contains a video
        )
        
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)

    # Forward message to log channel
    log_message = await update.forward(Config.TECH_VJ_LOG_CHANNEL)
    
    # Create log info message
    log_info = "Message Sender Information\n"
    log_info += f"\nFirst Name: {update.from_user.first_name}"
    log_info += f"\nUser ID: {update.from_user.id}"
    log_info += f"\nUsername: @{update.from_user.username}" if update.from_user.username else "\nUsername: N/A"
    log_info += f"\nUser Link: {update.from_user.mention}"

    # Check if the message is forwarded from another chat
    if update.forward_from:
        log_info += f"\nForwarded From: {update.forward_from.first_name} (@{update.forward_from.username})" if update.forward_from.username else f"\nForwarded From: {update.forward_from.first_name}"
    elif update.forward_from_chat:
        log_info += f"\nForwarded From Channel: {update.forward_from_chat.title}"

    # Reply to the forwarded message with user info
    await log_message.reply_text(
        text=log_info,
        disable_web_page_preview=True,
        quote=True
    )

    # Check if the message contains a video or file and forward it separately
    if update.video or update.document:
        try:
            # Send video or file to Log Channel
            if update.video:
                video_message = await bot.send_video(
                    chat_id=Config.TECH_VJ_LOG_CHANNEL,
                    video=update.video.file_id,
                    caption=f"🎥 Forwarded Video from {update.from_user.mention}"
                )
            elif update.document:
                file_message = await bot.send_document(
                    chat_id=Config.TECH_VJ_LOG_CHANNEL,
                    document=update.document.file_id,
                    caption=f"📄 Forwarded Document from {update.from_user.mention}"
                )
        except Exception as e:
            print(f"Error forwarding media/file: {e}")
