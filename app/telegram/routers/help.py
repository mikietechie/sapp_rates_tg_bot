from aiogram import filters, types, Router

help_router = Router(name=__name__)

HELP_CMD = types.BotCommand(command="help", description="How to use the Bot")
ABOUT_CMD = types.BotCommand(command="about", description="About the bot")
COMMANDS = [HELP_CMD, ABOUT_CMD]


@help_router.message(filters.Command(commands=[HELP_CMD.command]))
async def help_cmd(message: types.Message):
    await message.reply(
        text="Here is the bot manual",
    )


@help_router.message(filters.Command(commands=[ABOUT_CMD.command]))
async def about_cmd(message: types.Message):
    await message.reply(
        text="About the bot",
    )
