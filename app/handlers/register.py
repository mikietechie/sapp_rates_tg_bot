from aiogram import types, F, Router
from .forms_dispatcher import forms_dispatcher
from aiogram_forms.forms import Form, fields, FormsManager

from service import Service
import structs
import commands

router = Router(name=__name__)

REGISTER_FORM = "register-form"


@forms_dispatcher.register(REGISTER_FORM)
class RegisterForm(Form):
    email = fields.EmailField("Email", validators=[])
    password = fields.TextField("Password", min_length=2, validators=[])

    @classmethod
    async def callback(
        cls, message: types.Message, forms: FormsManager, **data
    ) -> None:
        data = await forms.get_data(REGISTER_FORM)
        try:
            data = structs.AuthCredentials(**data)
            obj = await Service.register(username=message.from_user.username, data=data)
            await message.answer(
                text=f"<pre>{obj.model_dump_json(indent=2)}</pre>",
                reply_markup=types.ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            types.KeyboardButton(
                                text=f"/{commands.ADD_CLIENT_CMD.command}"
                            ),
                        ],
                    ]
                ),
            )
        except Exception as e:
            await message.answer(
                text=f"Failed to Register.\n{e}",
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
                            types.KeyboardButton(text=f"No Thanks!"),
                        ],
                    ]
                ),
            )
            raise e


async def cmd_register(message: types.Message, forms: FormsManager) -> None:
    await forms.show(REGISTER_FORM)
