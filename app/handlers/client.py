from aiogram import types
from aiogram_forms.forms.manager import FormsManager

from service import Service


async def cmd_get_client(message: types.Message, forms: FormsManager):
    auth = Service.get_auth_data(message.from_user.username)
    client = await Service.get_client(auth)
    await message.answer(f"<pre>{client.model_dump_json(indent=2)}</pre>")
