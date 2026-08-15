import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
import config

# Bot and Userbot Client Setup
app = Client("MusicBot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
user_app = Client("MusicAssistant", api_id=config.API_ID, api_hash=config.API_HASH, session_string=config.STRING_SESSION)

call_py = PyTgCalls(user_app)

# Commands Menu Markup
COMMANDS_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("BACK", callback_data="cb_back"), InlineKeyboardButton("CLOSE", callback_data="cb_close")]
])

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    text = (
        "**COMMANDS**\n\n"
        "**REMOTE KERNEL SETUP**\n"
        "/join — JOIN RECORD & PLAY VC\n"
        "/leave — LEAVE BOTH VCS\n"
        "/leaveall — LEAVE BOTH VCS\n"
        "/leaverecord — LEAVE RECORD VC\n"
        "/leaveplay — LEAVE PLAY VC\n\n"
        "**AUDIO**\n"
        "/level — SET VOLUME 1–50\n"
        "/bass — SET BASS BOOST 0–15\n"
        "/treble — SET TREBLE BOOST 0–15\n"
        "/mute — MUTE ASSISTANT\n"
        "/unmute — UNMUTE ASSISTANT\n\n"
        "**SCREENSHARE**\n"
        "/screenshare — START SCREENSHARE\n"
        "/screenshareoff — STOP SCREENSHARE\n\n"
        "**RECORD**\n"
        "/startrecord — START RECORDING\n"
        "/stoprecord — STOP & UPLOAD\n\n"
        "**UTILS**\n"
        "/speedtest — RUN SPEEDTEST"
    )
    await message.reply_text(text, reply_markup=COMMANDS_MARKUP)

async def main():
    await app.start()
    await user_app.start()
    await call_py.start()
    print("Bot is running!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
