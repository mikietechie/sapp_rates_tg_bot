import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

import config
from routers import attach_dispatcher
from commands import COMMANDS
from log import logger


async def main():
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dispatcher = Dispatcher()
    attach_dispatcher(dispatcher)
    await bot.set_my_commands(COMMANDS)
    logger.info("Starting Telegram Polling")
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
