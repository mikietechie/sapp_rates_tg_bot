from aiogram import types


START_CMD = types.BotCommand(command="start", description="Start")
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
    LOGIN_CMD,
    REGISTER_CMD,
    LOGOUT_CMD,
    DEACTIVATE_CMD,
    USER_CMD,
    PAYMENT_CMD,
    GET_CLIENT_CMD,
    ADD_CLIENT_CMD,
]
