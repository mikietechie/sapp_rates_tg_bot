from aiogram import types

from service import Service
import commands


async def cmd_logout(message: types.Message) -> None:
    Service.logout(message.from_user.username)
    return await message.reply(
        text=f"Logged out successfully!",
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
