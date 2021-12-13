import os
import logging
import requests

from dotenv import load_dotenv

CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', None)
try:
    if len(CONFIG_FILE_URL) == 0:
        raise TypeError
    try:
        res = requests.get(CONFIG_FILE_URL)
        if res.status_code == 200:
            with open('../config.env', 'wb+') as f:
                f.write(res.content)
                f.close()
        else:
            logging.error(f"Failed to download config.env {res.status_code}")
    except Exception as e:
        logging.error(str(e))
except TypeError:
    pass

load_dotenv('config.env', override=True)


class Config(object):
    TG_BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    try:
        if len(TG_BOT_TOKEN) == 0:
            raise TypeError
    except TypeError:
        TG_BOT_TOKEN = None

    APP_ID = (os.environ.get('TELEGRAM_API', None))

    API_HASH = os.environ.get('TELEGRAM_HASH', None)

    CHANNEL_USERNAME = os.environ.get('CHANNEL_USERNAME', None)
    try:
        if len(CHANNEL_USERNAME) == 0:
            raise TypeError
    except TypeError:
        CHANNEL_USERNAME = None
