import os

from dotenv import load_dotenv

load_dotenv(override=True)
env = os.environ

# Server Conf
HOST = env.get("APP_HOST", "0.0.0.0")
PORT = int(env.get("APP_PORT", 8000))
PROD = env.get("ENV") == "production"

# Telegram Bot Conf
BOT_TOKEN = env.get("BOT_TOKEN")
BOT_PATH = "/bot"
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = "https://git-deploy-tg.the-devs.com" + BOT_PATH + WEBHOOK_PATH

