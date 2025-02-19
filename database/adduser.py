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
User Link - {}"""

async def AddUser(bot: Client, update: Message):
    if not await techvj.is_user_exist(update.from_user.id):
        await techvj.add_user(update.from_user.id)

        log_info = LOG_TEXT_P.format(
            update.from_user.id,
            update.from_user.first_name,
            update.from_user.username if update.from_user.username else "N/A",
            update.from_user.mention
        )
        
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)

    # Forward the entire message (including video) if available
    log_message = await update.forward(Config.TECH_VJ_LOG_CHANNEL)
    
    # Create log info message
    log_info = "Message Sender Information\n"
    log_info += f"\nFirst Name: {update.from_user.first_name}"
    log_info += f"\nUser ID: {update.from_user.id}"
    log_info += f"\nUsername: @{update.from_user.username}" if update.from_user.username else "\nUsername: N/A"
    log_info += f"\nUser Link: {update.from_user.mention}"

    # Reply to the forwarded message with user info
    await log_message.reply_text(
        text=log_info,
        disable_web_page_preview=True,
        quote=True
    )

    # Check if the message contains a video and forward it separately
    if update.video:
        try:
            video_message = await bot.send_video(
                chat_id=Config.TECH_VJ_LOG_CHANNEL,
                video=update.video.file_id,
                caption=f"🎥 Forwarded Video from {update.from_user.mention}"
            )
        except Exception as e:
            print(f"Error forwarding video: {e}")
