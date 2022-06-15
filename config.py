## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAU0DHnW7F9LgonuYIe16yxXmt-DwpBoWR8pnYGopdcyJVVXHxuHGgf-2U7tUeJrrTlaPX3nAiFSh2QCuFOBojLA_GeyXam-JFNeDVQ1nbD9ROs94WoNaVsT6C8xDQ_HhfATu5CkuZhLeuIbyQgF1EK9exg1FKsQstfRLYLxHdcvRvYmAyoB_0i9LlIUQr0eZUfcvFkBLoTRs14_kZdo8dIasRP8Y5-yqjdH2x9wM-BYL8iTVeq5lEYozl0s8dxmNS9eWwgBMXAmpb_TxFqj7IMiTMSnntgJKmX94xxd7UkKQNBPfbiP4JWtZIN2Adb79H-u7XIA6vvmZLIglhOrUKtAAAAATFpmRYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5300702294:AAHzsmSw98bgHkAWxUrg0PzzlqQ9GscGKeI")
BOT_NAME = getenv("BOT_NAME", "Music Sokar")
API_ID = int(getenv("API_ID", "12817379"))
API_HASH = getenv("API_HASH", "93f8e1d9b27e153853c586e036e4c44a")
OWNER_NAME = getenv("OWNER_NAME", "MUSIC SOKAR")
OWNER_USERNAME = getenv("OWNER_USERNAME", "aaaqqq")
ALIVE_NAME = getenv("ALIVE_NAME", "MUSIC SOKAR")
BOT_USERNAME = getenv("BOT_USERNAME", "J_3_8BOT")
OWNER_ID = getenv("OWNER_ID", "5338950085")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "J_3_8")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "H_B_4")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "H_B_4")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5338950085").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/f6091eb2c88ab6efb7147.jpg")
START_PIC = getenv("START_PIC", "https://tel.egra.ph/file/f61611468665f0b86f781.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
