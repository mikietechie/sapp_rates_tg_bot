from aiogram import Bot, Dispatcher, types, F

import config
from .routers import setup_dispatcher
from commands import COMMANDS


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dispatcher = Dispatcher()


async def set_bot_commands():
    await bot.set_my_commands(COMMANDS)



async def bootstrap_bot():
    print("Bootstrapping bot")
    setup_dispatcher(dispatcher)
    await set_bot_commands()
    print("Telegram polling")
    await dispatcher.start_polling(bot)
