import re
import os
from os import environ
from pyrogram import enums
import asyncio
import json
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.strip().lower() in ["on", "true", "yes", "1", "enable", "y"]: return True
    elif value.strip().lower() in ["off", "false", "no", "0", "disable", "n"]: return False
    else: return default

API_ID = int(os.environ.get('API_ID', '27874328'))
API_HASH = os.environ.get('API_HASH', '9dd30a06ae04f1b3fb44b02f22e99624')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8057019885:AAHpn9T0XQv2NOB6kJqy_kI75YoMciHiPQY')
PORT = os.environ.get("PORT", "8080")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1204889321 2144812475')]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001786472360'))

# for mongodb
DATABASE_NAME = os.environ.get("DB_NAME", "auto")     
DATABASE_URI  = os.environ.get("DB_URL", "mongodb+srv://hi:hi@auto.natzh.mongodb.net/?retryWrites=true&w=majority&appName=auto")
MONGO_URL = os.environ.get('MONGO_URL', "")



