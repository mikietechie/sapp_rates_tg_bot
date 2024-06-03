from aiogram import types, F, Router
from .forms_dispatcher import forms_dispatcher
from aiogram_forms.forms import Form, fields, FormsManager

from service import Service
import structs
import commands

router = Router(name=__name__)

LOGIN_FORM = "login-form"


@forms_dispatcher.register(LOGIN_FORM)
class LoginForm(Form):
    email = fields.EmailField("Email", validators=[])
    password = fields.TextField("Password", min_length=2, validators=[])

    @classmethod
    async def callback(
        cls, message: types.Message, forms: FormsManager, **data
    ) -> None:
        data = await forms.get_data(LOGIN_FORM)
        try:
            creds = structs.AuthCredentials(**data)
            obj = await Service.login(username=message.from_user.username, creds=creds)
            await message.answer(
                text=f"<pre>{obj.model_dump_json(indent=2)}</pre>",
                reply_markup=types.ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            types.KeyboardButton(
                                text=f"/{commands.GET_CLIENT_CMD.command}"
                            ),
                        ],
                        [
                            types.KeyboardButton(text=f"Ok Cool!"),
                        ],
                    ]
                ),
            )
        except Exception as e:
            await message.answer(
                text=f"Failed to Login.\n{e}",
                reply_markup=types.ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            types.KeyboardButton(text=f"/{commands.LOGIN_CMD.command}"),
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


async def cmd_login(message: types.Message, forms: FormsManager) -> None:
    await forms.show(LOGIN_FORM)