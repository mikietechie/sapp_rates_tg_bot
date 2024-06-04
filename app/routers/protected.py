from aiogram.filters import Command
from aiogram import Router

from middleware.auth import AuthMiddleware
from middleware.error import ErrorMiddleware
from commands import USER_CMD, GET_CLIENT_CMD, LOGOUT_CMD
from handlers.user import cmd_user
from handlers.client import cmd_get_client
from handlers.logout import cmd_logout

router = Router(name=__name__)
router.message.middleware(ErrorMiddleware())
router.message.middleware(AuthMiddleware())


router.message(Command(commands=[USER_CMD.command]))(cmd_user)
router.message(Command(commands=[LOGOUT_CMD.command]))(cmd_logout)
router.message(Command(commands=[GET_CLIENT_CMD.command]))(cmd_get_client)
