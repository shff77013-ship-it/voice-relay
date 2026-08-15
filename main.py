import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Fake Port Server for Render Web Service
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Alive!")

def run_health_check_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_health_check_server, daemon=True).start()

# Environment Variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Client("RelayBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Command Text Layout
COMMAND_TEXT = (
    "📋 **COMMANDS**\n\n"
    "🔗 **REMOTE KERNEL SETUP**\n"
    "`/join` — JOIN RECORD & PLAY VC\n"
    "`/leave` — LEAVE BOTH VCS\n"
    "`/leaveall` — LEAVE BOTH VCS\n"
    "`/leaverecond` — LEAVE RECORD VC\n"
    "`/leaveplay` — LEAVE PLAY VC\n\n"
    "🔊 **AUDIO**\n"
    "`/level` — SET VOLUME 1–50\n"
    "`/bass` — SET BASS BOOST 0–15\n"
    "`/treble` — SET TREBLE BOOST 0–15\n"
    "`/mute` — MUTE ASSISTANT\n"
    "`/unmute` — UNMUTE ASSISTANT\n\n"
    "🖥️ **SCREENSHARE**\n"
    "`/screenshare` — START SCREENSHARE\n"
    "`/screenshareoff` — STOP SCREENSHARE\n\n"
    "⏺️ **RECORD**\n"
    "`/startrecord` — START RECORDING\n"
    "`/stoprecord` — STOP & UPLOAD\n\n"
    "⚡ **UTILS**\n"
    "`/speedtest` — RUN SPEEDTEST"
)

# Inline Keyboard Markup
START_BUTTONS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🔙 BACK", callback_data="back_menu")],
        [InlineKeyboardButton("❌ CLOSE", callback_data="close_menu")]
    ]
)

# Start Command Handler
@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(
        text=COMMAND_TEXT,
        reply_markup=START_BUTTONS
    )

# Callback Query Handler for Buttons
@bot.on_callback_query()
async def callback_handler(client, query: CallbackQuery):
    if query.data == "close_menu":
        await query.message.delete()
    elif query.data == "back_menu":
        await query.answer("You are already on the main menu!", show_alert=True)

async def main():
    await bot.start()
    print(">>> Sigma Fighter Bot Started Successfully <<<")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
