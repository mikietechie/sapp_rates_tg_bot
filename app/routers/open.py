from aiogram import Router
from aiogram.filters import CommandStart, Command

import commands
from handlers.start import cmd_start
from handlers.login import cmd_login
from handlers.help import cmd_help
from handlers.about import cmd_about

router = Router(name=__name__)

router.message(CommandStart())(cmd_start)
router.message(Command(commands=[commands.LOGIN_CMD.command]))(cmd_login)
router.message(Command(commands=[commands.HELP_CMD.command]))(cmd_help)
router.message(Command(commands=[commands.ABOUT_CMD.command]))(cmd_about)
