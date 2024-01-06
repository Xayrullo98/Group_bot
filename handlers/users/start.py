from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters.shaxsiy import Shaxsiy

@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
