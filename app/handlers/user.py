from aiogram import types

from service import Service


async def cmd_user(message: types.Message):
    auth = Service.get_auth_data(message.from_user.username)
    return await message.answer(
        text=f"<pre>{auth.user.model_dump_json(indent=2)}</pre>"
    )
