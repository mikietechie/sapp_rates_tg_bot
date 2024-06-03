import json

from aiogram import types

import cache
import structs
import commands
from service import Service


async def cmd_start(message: types.Message):
    auth = Service.get_auth_data(message.from_user.username)
    if auth:
        return await message.reply(
            text=f"Hello {auth.user.email}",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[
                    [
                        types.KeyboardButton(
                            text=f"/{commands.GET_CLIENT_CMD.command}"
                        ),
                    ],
                    [
                        types.KeyboardButton(text=f"/{commands.USER_CMD.command}"),
                    ],
                    [
                        types.KeyboardButton(text=f"/{commands.LOGOUT_CMD.command}"),
                    ],
                    [
                        types.KeyboardButton(text=f"Ok Cool!"),
                    ],
                ]
            ),
        )
    return await message.reply(
        text=f"Hello, welcome",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text=f"/{commands.REGISTER_CMD.command}"),
                ],
                [
                    types.KeyboardButton(text=f"/{commands.LOGIN_CMD.command}"),
                ],
                [
                    types.KeyboardButton(text=f"Ok Cool!"),
                ],
            ]
        ),
    )
