import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
import requests
from mysecrets import *
import openai
import os
import subprocess

openai.api_key = openai_api_key
async def main():
    client = TelegramClient('session', api_id, api_hash)

    @client.on(events.NewMessage)
    async def handler(event):
        # Check if the message is a voice message
        if event.message.voice or event.message.audio:
            # Download the voice message
            print("Downloading voice message")
            print(event.message)
            voice_message = await client.download_media(event.message.voice or event.message.audio)
            [file, ext] = os.path.splitext(voice_message)
            print(file, ext)
            if ext not in [".mp3", ".mp4", ".mpeg", ".mpga", ".m4a", ".wav", ".webm"]:
              converted_file = file + ".mp3"
              subprocess.run(['ffmpeg', '-y', '-i', voice_message, converted_file])
              if os.path.isfile(voice_message):
                os.remove(voice_message)
              voice_message = converted_file

            # Transcribe the voice message using Whisper API
            with open(voice_message, 'rb') as f:
              print("Transcribing voice message")
              #transcription = openai.Audio.transcribe("whisper-1", f, language="it")
              transcription = openai.Audio.transcribe("whisper-1", f)

            if transcription:
                if os.path.isfile(voice_message):
                  os.remove(voice_message)
                # Forward the transcribed text to your custom bot
                print(transcription)

                entity = 'anon'
                sender = await event.get_sender()
                if sender and sender.username:
                  entity = sender.username
                elif sender and sender.title:
                  entity = sender.title

                message = transcription.text + "\n\nFrom " + entity

                bot = TelegramClient('bot', api_id, api_hash)
                await bot.start(bot_token=bot_token)
                await bot.send_message(myself_id, message)
                await bot.disconnect()
            else:
                print("Error transcribing the voice message:")

    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())

