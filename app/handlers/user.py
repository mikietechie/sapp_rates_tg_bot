from aiogram import types

from structs import AuthDataModel


async def cmd_user(message: types.Message, auth: AuthDataModel):
    return await message.answer(
        text=f"<pre>{auth.user.model_dump_json(indent=2)}</pre>"
    )
