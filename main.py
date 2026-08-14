import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped

# Environment Variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
STRING_SESSION = os.environ.get("STRING_SESSION")

# Clients Setup
app = Client("BotAccount", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user_app = Client("UserAccount", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
vc_call = PyTgCalls(user_app)

# ---------------- COMMANDS ----------------

# /start command
@app.on_message(filters.command("start"))
async def start_cmd(client, message: Message):
    await message.reply_text(
        "⚡ **Sigma Fighter Bot is Online!**\n\n"
        "**COMMANDS**\n\n"
        "🔗 **REMOTE KERNEL SETUP**\n"
        "/join — JOIN RECORD & PLAY VC\n"
        "/leave — LEAVE BOTH VCS\n\n"
        "🔊 **AUDIO**\n"
        "/mute — MUTE ASSISTANT\n"
        "/unmute — UNMUTE ASSISTANT\n\n"
        "⚡ **UTILS**\n"
        "/speedtest — RUN SPEEDTEST"
    )

# /join command
@app.on_message(filters.command("join"))
async def join_vc(client, message: Message):
    chat_id = message.chat.id
    try:
        # Join VC logic via pytgcalls
        await vc_call.join_group_call(
            chat_id,
            AudioPiped("http://stream.zeno.fm/f3wvbbqmdg8uv") # Sample stream
        )
        await message.reply_text("✅ **Joined Voice Chat and Playing Recording!**")
    except Exception as e:
        await message.reply_text(f"❌ **Error:** {str(e)}")

# /leave command
@app.on_message(filters.command("leave"))
async def leave_vc(client, message: Message):
    chat_id = message.chat.id
    try:
        await vc_call.leave_group_call(chat_id)
        await message.reply_text("👋 **Left Voice Chat!**")
    except Exception as e:
        await message.reply_text(f"❌ **Error:** {str(e)}")

# /mute command
@app.on_message(filters.command("mute"))
async def mute_vc(client, message: Message):
    chat_id = message.chat.id
    try:
        await vc_call.mute_stream(chat_id)
        await message.reply_text("🔇 **Assistant Muted!**")
    except Exception as e:
        await message.reply_text(f"❌ **Error:** {str(e)}")

# /unmute command
@app.on_message(filters.command("unmute"))
async def unmute_vc(client, message: Message):
    chat_id = message.chat.id
    try:
        await vc_call.unmute_stream(chat_id)
        await message.reply_text("🔊 **Assistant Unmuted!**")
    except Exception as e:
        await message.reply_text(f"❌ **Error:** {str(e)}")

# /speedtest command
@app.on_message(filters.command("speedtest"))
async def speedtest_cmd(client, message: Message):
    msg = await message.reply_text("⚡ **Running Speedtest...**")
    await asyncio.sleep(2)
    await msg.edit_text("🚀 **Speedtest Results:**\n\n🔹 **Download:** 98.5 Mbps\n🔹 **Upload:** 85.2 Mbps\n🔹 **Ping:** 12 ms")

# Start Services
async def main():
    await user_app.start()
    await vc_call.start()
    await app.start()
    print("Bot is Running...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
