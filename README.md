# fuck_voice_messages.py
A telegram bot that transcribes incoming voice messages into text using ffmpeg and Whisper

## Install Requirements
```bash
pip3 install asyncio telethon requests openai
```

## Fill secrets
```bash
cp mysecrets.py.copy mysecrets.py
```
Then fill in the bot id, user id, openai api_key etc

## Run
```bash
python3 fuck_voice_messages.py
```

## Test
With `fuck_voice_messages.py` running, run 
```bash
python3 test/test_audio_message.py
python3 test/test_voice_message.py
```

To check that messages are transcribed correctly
