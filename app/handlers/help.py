from aiogram import types

import config
import commands

commands = "\n".join(["/" + cmd.command for cmd in commands.COMMANDS])

HELP_TEXT = """
<b>SAPP Finance User Bot | Help</b>\n\n
Type "/" and you will get a hint of the supported Commands\n
FAQS
1. If you get a 403 err, please logout and login again.\n
2. Visit the API Docs {0}/docs/index.html\n
Commands\n{1}
""".format(
    config.SERVER_URL, commands
)


async def cmd_help(message: types.Message):
    await message.answer(text=HELP_TEXT)
