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
        
        log_info = LOG_TEXT_P.format(update.from_user.id, update.from_user.mention)
        log_info += "\nUsername: @" + (update.from_user.username if update.from_user.username else "N/A")
        log_info += "\nUser Link: " + update.from_user.mention
        
        await bot.send_message(Config.TECH_VJ_LOG_CHANNEL, log_info)

    # Forward message to log channel
    log_message = await update.forward(Config.TECH_VJ_LOG_CHANNEL)
    
    # Create log info message
    log_info = "Message Sender Information\n"
    log_info += "\nFirst Name: " + update.from_user.first_name
    log_info += "\nUser ID: " + str(update.from_user.id)
    log_info += "\nUsername: @" + (update.from_user.username if update.from_user.username else "N/A")
    log_info += "\nUser Link: " + update.from_user.mention

    # Reply to the forwarded message with user info
    await log_message.reply_text(
        text=log_info,
        disable_web_page_preview=True,
        quote=True
    )
