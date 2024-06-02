from aiogram import types, filters, F, Router
from aiogram_forms.forms import FormsManager

import commands
import utils
from forms.login import LOGIN_FORM

router = Router(name=__name__)

@router.message(filters.Command(commands=[commands.LOGIN_CMD.command]))
async def handle_login(message: types.Message, forms: FormsManager) -> None:
    await forms.show(LOGIN_FORM)

@router.message(filters.Command(commands=[commands.USER_CMD.command]))
async def handle_user(message: types.Message, forms: FormsManager) -> None:
    user = utils.get_auth_data(message.from_user.username)
    if user:
        await message.answer(
            text=user.model_dump_json
        )
        return
    await message.answer(
        text=f"Wadiii",
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

@router.message(filters.Command(commands=[commands.REGISTER_CMD.command]))
async def handle_register(message: types.Message, forms: FormsManager) -> None:
    await forms.show(LOGIN_FORM)

@router.message(filters.Command(commands=[commands.LOGOUT_CMD.command]))
async def handle_logout(message: types.Message, forms: FormsManager) -> None:
    await forms.show(LOGIN_FORM)

