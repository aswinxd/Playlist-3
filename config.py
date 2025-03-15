# +++ Made By King [telegram username: @Shidoteshika1] +++

import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler



TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8141368818:AAFQXS4KI1R7Nm4dANZ8nje1wTpCUCE2_Og")


APP_ID = int(os.environ.get("APP_ID", "12799559"))


API_HASH = os.environ.get("API_HASH", "077254e69d93d08357f25bb5f4504580")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001767426891"))


OWNER_ID = int(os.environ.get("OWNER_ID", "6854172577"))


SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "")


PORT = os.environ.get("PORT", "8570")


DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://mdalizadeh16:lavos@cluster0.u21tcwa.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DATABASE_NAME", "PLaylist-1")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "20"))

PICS = (os.environ.get("PICS", "https://graph.org/file/9857bdab22a1540153879-45f5141823c9228c50.jpg")).split() #Required


CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
