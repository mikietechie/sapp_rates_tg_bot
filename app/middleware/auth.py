from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram import types

from service import Service
import commands


class AuthMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        auth = Service.get_auth_data(event.from_user.username)
        if not auth:
            await event.reply(
                text=f"No User Was Found ",
                reply_markup=types.ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            types.KeyboardButton(
                                text=f"/{commands.LOGIN_CMD.command}"
                            ),
                        ],
                        [
                            types.KeyboardButton(
                                text=f"/{commands.REGISTER_CMD.command}"
                            ),
                        ],
                        [
                            types.KeyboardButton(text=f"Ok Cool!"),
                        ],
                    ]
                ),
            )
            return
        data['auth'] = auth
        return await handler(event, data)