from aiogram import Dispatcher

from handlers.forms_dispatcher import forms_dispatcher
from . import protected, open


def attach_dispatcher(dispatcher: Dispatcher):
    forms_dispatcher.attach(dispatcher)
    dispatcher.include_routers(
        open.router,
        protected.router
    )
