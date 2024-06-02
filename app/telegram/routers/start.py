import json

from aiogram import types, filters, F, Router

import cache
import structs
import commands

start_router = Router(name=__name__)


@start_router.message(filters.CommandStart())
async def cmd_start(message: types.Message):
    user = cache.rds.get(f"{message.from_user.username}")
    if user:
        print(user)
        auth = structs.AuthDataModel(**json.loads(user))
        print(auth.model_dump_json())
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
                                types.KeyboardButton(
                                    text=f"/{commands.USER_CMD.command}"
                                ),
                            ],
                            [
                                types.KeyboardButton(
                                    text=f"/{commands.LOGOUT_CMD.command}"
                                ),
                            ],
                            [
                                types.KeyboardButton(text=f"Ok Cool!"),
                            ],
                        ]
                    ),
        )
    return await message.reply(
        text=f"Hello World", 
                reply_markup=types.ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            types.KeyboardButton(
                                text=f"/{commands.REGISTER_CMD.command}"
                            ),
                        ],
                        [
                            types.KeyboardButton(
                                text=f"/{commands.LOGIN_CMD.command}"
                            ),
                        ],
                        [
                            types.KeyboardButton(text=f"Ok Cool!"),
                        ],
                    ]
                ),
    )
