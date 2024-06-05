from aiogram import types

import config
from service import Service


async def cmd_payments(message: types.Message):
    auth = Service.get_auth_data(message.from_user.username)
    client = await Service.get_client(auth)
    await message.answer(
        text="<b>SAPP Finance User Bot | Payments</b>\n\n{0}/payments/{1}\n\n".format(
            config.SERVER_URL, client.ID
        )
    )
