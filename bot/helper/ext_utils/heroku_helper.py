import asyncio
import os
import shlex
import heroku3

from functools import wraps
from pyrogram.types import Message
from typing import Tuple
from bot import HEROKU_API_KEY, HEROKU_APP_NAME

# Reimplement by https://github.com/arshsisodiya
# Setting Message

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None

# Preparing For Setting Config
# Reimplement by https://github.com/arshsisodiya and Based on this https://github.com/DevsExpo/FridayUserbot/blob/master/plugins/heroku_helpers.py

heroku_client = None
if HEROKU_API_KEY:
    heroku_client = heroku3.from_key(HEROKU_API_KEY)

def check_heroku(func):
    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await message.reply_text("`Please Add HEROKU_API_KEY Key For This To Function To Work!`", parse_mode="markdown")
        elif not HEROKU_APP_NAME:
            await message.reply_text("`Please Add HEROKU_APP_NAME For This To Function To Work!`", parse_mode="markdown")
        if HEROKU_APP_NAME and heroku_client:
            try:
                heroku_app = heroku_client.app(HEROKU_APP_NAME)
            except:
                await message.reply_text(message, "`Heroku Api Key And App Name Doesn't Match!`", parse_mode="markdown")
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli