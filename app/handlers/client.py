from aiogram import types
from aiogram_forms.forms import Form, fields, FormsManager

from service import Service
import structs
from .forms_dispatcher import forms_dispatcher


ClIENT_FORM = "client-form"


@forms_dispatcher.register(ClIENT_FORM)
class ClientForm(Form):
    name = fields.TextField("Name", min_length=3)
    domains = fields.TextField("Domains", min_length=1)

    @classmethod
    async def callback(
        cls, message: types.Message, forms: FormsManager, **kwargs
    ) -> None:
        form_data = await forms.get_data(ClIENT_FORM)
        data = structs.CreateClient(**form_data)
        obj = await Service.create_client(
            auth=Service.get_auth_data(message.from_user.username), data=data
        )
        await message.answer(text=f"<pre>{obj.model_dump_json(indent=2)}</pre>")


async def cmd_add_client(message: types.Message, forms: FormsManager) -> None:
    await forms.show(ClIENT_FORM)


async def cmd_get_client(message: types.Message, forms: FormsManager):
    auth = Service.get_auth_data(message.from_user.username)
    client = await Service.get_client(auth)
    await message.answer(f"<pre>{client.model_dump_json(indent=2)}</pre>")
