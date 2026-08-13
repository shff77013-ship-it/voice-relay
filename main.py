import asyncio
import os
from pyrogram import Client, filters
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

# Start HTTP Server in background thread
threading.Thread(target=run_health_check_server, daemon=True).start()

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
STRING_SESSION = os.environ.get("STRING_SESSION")

bot = Client("RelayBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
user = Client("RelayUser", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🔥 Voice Chat Relay Bot is Live!")

async def main():
    await bot.start()
    await user.start()
    print(">>> Relay Bot Started Successfully <<<")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
