import asyncio
import os
from pyrogram import Client, filters

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
    print(">>> Relay Bot Started <<<")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
