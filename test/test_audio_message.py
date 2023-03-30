import os
from telethon import TelegramClient, types, events
from mysecrets import *

# Replace the value below with the full path to the MP3 file you want to send as a voice message.
mp3_file = './test.mp3'

# Create a new TelegramClient instance.
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Define a function to send a voice message with the specified MP3 file.
async def send_voice_message():
    await bot.send_file(myself_id, mp3_file)

# Start the client and send the voice message.
with bot:
    bot.loop.run_until_complete(send_voice_message())

