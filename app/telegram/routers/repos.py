import re, random

from aiogram import types, filters, F, Router
from aiogram_forms import dispatcher
from aiogram_forms.forms import Form, fields, FormsManager

# from aiogram_forms.errors import ValidationError

from documents import RepositoryDoc
from .validators.number import IntValidator

router = Router(name=__name__)

ADD_CMD = types.BotCommand(command="add_repo", description="Create new Repo")
DELETE_CMD = types.BotCommand(command="delete_repo", description="Delete Repo")
LIST_CMD = types.BotCommand(command="list_repo", description="List All Repos")
VIEW_CMD = types.BotCommand(command="view_repo", description="View Repo")
COMMANDS = [LIST_CMD, ADD_CMD]

REPO_FORM = "repo-form"


@dispatcher.register(REPO_FORM)
class RepoForm(Form):
    project_id = fields.TextField(
        "Project ID", min_length=2, validators=[IntValidator()]
    )

    @classmethod
    async def callback(
        cls, message: types.Message, forms: FormsManager, **data
    ) -> None:
        data = await forms.get_data(REPO_FORM)
        doc = RepositoryDoc(**data)
        doc.set_from_gitlab()
        await doc.save()
        await message.answer(
            text=f"{doc.project_id} repo has been saved!!",
            reply_markup=types.ReplyKeyboardMarkup(
                keyboard=[
                    [
                        types.KeyboardButton(text=f"/{ADD_CMD.command}"),
                    ],
                    [
                        types.KeyboardButton(text=f"/{LIST_CMD.command}"),
                    ],
                    [
                        types.KeyboardButton(text=f"Ok Cool!"),
                    ],
                ]
            ),
        )


@router.message(filters.Command(commands=[ADD_CMD.command]))
async def add_repo(message: types.Message, forms: FormsManager) -> None:
    await forms.show(REPO_FORM)


@router.message(filters.Command(commands=[LIST_CMD.command]))
async def list_repo(message: types.Message, forms: FormsManager) -> None:
    kbd = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text=f"/{ADD_CMD.command}"),
            ],
            [
                types.KeyboardButton(text=f"Ok Cool!"),
            ],
        ]
    )
    docs = await RepositoryDoc.find_all().to_list()
    if not len(docs):
        await message.reply(text="No Repos found!", reply_markup=kbd)
        return
    text = f"\n{'*'*10}\n".join(
        [
            (
                f"project: {doc.project_id}\n"
                f"name: {doc.name}\n"
                f"url : {doc.url}\n\n"
                f"/{VIEW_CMD.command}_{doc.id}\n\n"
            )
            for doc in docs
        ]
    )

    await message.reply(text=text, reply_markup=kbd)


@router.message(filters.Command(re.compile(f"^{DELETE_CMD.command}*")))
async def delete_repo(message: types.Message, forms: FormsManager) -> None:
    doc_id = message.text.split(DELETE_CMD.command)[-1][1:]
    doc = await RepositoryDoc.get(doc_id)
    if not doc:
        await message.reply(text=f"Repo with {doc_id} was not found!")
        return
    await doc.delete()
    await message.reply(text=f"Deleted repo {doc.name}")


@router.message(filters.Command(re.compile(f"^{VIEW_CMD.command}*")))
async def view_repo(message: types.Message, forms: FormsManager) -> None:
    doc_id = message.text.split(VIEW_CMD.command)[-1][1:]
    doc = await RepositoryDoc.get(doc_id)
    if not doc:
        await message.reply(text=f"Repo with {doc_id} was not found!")
        return
    kbd = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text=f"/{DELETE_CMD.command}_{doc.id}"),
            ],
            [
                types.KeyboardButton(text=f"Ok"),
            ],
        ]
    )
    await message.reply(
        text=(
            f"<pre>{doc.model_dump_json(indent=2)}</pre>"
            f"{random.choice(['⛔️','🟢','⚪️',])} is running"
        ),
        reply_markup=kbd,
    )
