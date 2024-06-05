from aiogram import types


START_CMD = types.BotCommand(command="start", description="Start")
ABOUT_CMD = types.BotCommand(command="about", description="About")
HELP_CMD = types.BotCommand(command="help", description="Help")
DOCS_CMD = types.BotCommand(command="docs", description="Docs")
LOGIN_CMD = types.BotCommand(command="login", description="Login")
REGISTER_CMD = types.BotCommand(command="register", description="Register")
LOGOUT_CMD = types.BotCommand(command="logout", description="Logout")
DEACTIVATE_CMD = types.BotCommand(command="deactivate", description="Deactivate")
USER_CMD = types.BotCommand(command="user", description="User")
PAYMENT_CMD = types.BotCommand(command="make_payment", description="Make Payment")
GET_CLIENT_CMD = types.BotCommand(command="get_client", description="Get Client")
ADD_CLIENT_CMD = types.BotCommand(command="add_client", description="Add Client")

COMMANDS = [
    START_CMD,
    GET_CLIENT_CMD,
    USER_CMD,
    PAYMENT_CMD,
    LOGIN_CMD,
    LOGOUT_CMD,
    HELP_CMD,
    ABOUT_CMD,
    DEACTIVATE_CMD,
    ADD_CLIENT_CMD,
    REGISTER_CMD,
]
