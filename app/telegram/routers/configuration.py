from aiogram import Bot, Dispatcher, types, filters, F, Router
from aiogram_forms import dispatcher as configuration_dispatcher
from aiogram_forms.forms import Form, fields, FormsManager
# from aiogram_forms.errors import ValidationError

from documents import RepositoryConfigurationDoc

router = Router(name=__name__)

UPDATE_CMD = types.BotCommand(
    command="set_configuration",
    description="Update configuration"
)
VIEW_CMD = types.BotCommand(
    command="view_configuration",
    description="Detail configuration"
)
COMMANDS = [VIEW_CMD, UPDATE_CMD]


@configuration_dispatcher.register('configuration-form')
class ConfigurationForm(Form):
    title = fields.TextField('Title', min_length=2, validators=[])
    username = fields.TextField('Username', min_length=2, validators=[])
    token = fields.TextField('token', min_length=2, validators=[])

    @classmethod
    async def callback(cls, message: types.Message, forms: FormsManager, **data) -> None:
        # Get form data from state
        data = await forms.get_data('configuration-form')
        doc = await RepositoryConfigurationDoc.find_one({})
        if doc:
            for (k, v) in data.items():
                if v:
                    setattr(doc, k, v)
        else:
            doc = RepositoryConfigurationDoc(**data)
        await doc.save()
        await message.answer(
            text=f'Default repo configuration has been saved!!',
            # Use this for reset if last field contains keyboard
            reply_markup=types.ReplyKeyboardRemove()
        )


@router.message(filters.Command(commands=[UPDATE_CMD.command]))
async def add_configuration(message: types.Message, forms: FormsManager) -> None:
    await forms.show('configuration-form')


@router.message(filters.Command(commands=[VIEW_CMD.command]))
async def view_configuration(message: types.Message, forms: FormsManager) -> None:
    kbd = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text=f"/{UPDATE_CMD.command}"),
            ],
            [
                types.KeyboardButton(text=f"Ok Cool!"),
            ],
        ]
    )
    doc = await RepositoryConfigurationDoc.find_one({})
    if not doc:
        await message.reply(
            text="Default conf is not yet set!",
            reply_markup=kbd
        )
        return
    await message.reply(
        text=f"<pre>{doc.model_dump_json(indent=2)}</pre>",
        reply_markup=kbd
    )
    # await message.reply(
    #     text=(
    #         f"Title           \t:\t{doc.title}\n"
    #         f"Username \t:\t{doc.username}\n"
    #         f"Token        \t:\t{doc.token}\n"
    #     ),
    #     reply_markup=kbd
    # )
