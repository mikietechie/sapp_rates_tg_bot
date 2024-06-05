from aiogram import types

ABOUT_TEXT = f"""
<b>SAPP Finance User Bot | About</b>\n\n
This is a Telegram service to help you setup and manage your SAPP Finance API service.\n\n
Here you can do the following:\n
1. Register\n
2. Login\n
3. Create a Client\n
4. Get your API key\n
5. Get you API token\n
6. Check your balance\n
7. Make payments for your API\n
8. Logout\n
"""


async def cmd_about(message: types.Message):
    await message.answer(text=ABOUT_TEXT)