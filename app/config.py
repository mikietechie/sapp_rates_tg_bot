import os

from dotenv import load_dotenv

load_dotenv(override=True)
env = os.environ

# Server Conf
PROD = env.get("ENV") == "production"
SERVER_URL = env.get("SERVER_URL") or "http://localhost:8000"
API_URL = SERVER_URL + "/api/v1"

# Redis
REDIS_HOST = env.get("REDIS_HOST") or "localhost"
REDIS_PORT = int(env.get("REDIS_PORT") or "6379")
REDIS_DB = int(env.get("REDIS_DB") or "0")
REDIS_PASSWORD = env.get("REDIS_PASSWORD")

# Telegram Bot Conf
BOT_TOKEN = env.get("BOT_TOKEN")
