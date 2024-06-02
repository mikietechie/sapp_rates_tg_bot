from aiogram import Dispatcher

from forms.forms_dispatcher import forms_dispatcher
from . import auth, start, help


def setup_dispatcher(dispatcher: Dispatcher):
    forms_dispatcher.attach(dispatcher)
    # configuration.configuration_dispatcher.attach(dispatcher)
    dispatcher.include_routers(
        start.start_router,
        # repos.router,
        help.help_router,
        auth.router
    )
