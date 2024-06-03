from aiogram import types

async def cmd_about(message: types.Message):
    await message.answer("About us")