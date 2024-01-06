from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from data.config import kanallar
from keyboards.default.tasdiq import tasdiq_buttons
from states.ads_states import AdsState
from loader import dp, bot
from filters.shaxsiy import Shaxsiy
from keyboards.inline.inline_for import ads_button


@dp.message_handler(Shaxsiy(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")


@dp.message_handler(Shaxsiy(), commands="Reklama", chat_id="6570924683")
async def bot_start(message: types.Message):
    await message.answer(f"Postni kiriting, {message.from_user.full_name}!")
    await AdsState.post.set()


@dp.message_handler(Shaxsiy(), state=AdsState.post)
async def bot_start(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data({"post": text})
    buttons = await ads_button(channels=kanallar)
    await message.answer(text="Guruhlarni tanlang", reply_markup=buttons)
    await AdsState.channel.set()


@dp.callback_query_handler(state=AdsState.channel)
async def bot_start(message: CallbackQuery, state: FSMContext):
    text = message.data
    if text == 'all':
        await state.update_data({"channels": "all"})
    elif text == "confirm":
        data = await state.get_data()
        post = data.get("post")
        msg = f'{post}\n'

        await bot.send_message(chat_id=message.from_user.id, text=msg)

        await bot.send_message(chat_id=message.from_user.id,text="Jo'natish uchun tasdiqlash tugmasini bosing",
                               reply_markup=tasdiq_buttons)
        await AdsState.confirm.set()
    # else:
    #     await state.update_data({"channels": {f"{text}": text}})
    #     await message.answer(text="Guruhlarni tanlang")
    #     await AdsState.channel.set()


@dp.message_handler(Shaxsiy(), state=AdsState.confirm, text="Tasdiqlash")
async def bot_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    post = data.get("post")
    msg = f'{post}\n'
    chnls = [i for i in kanallar]
    for j in chnls:
        try:
            await bot.send_message(chat_id=f"{j}", text=msg)
        except Exception as x:
            await bot.send_message(chat_id="6570924683", text=f"{x}")
    await state.finish()


@dp.message_handler(Shaxsiy(), state=AdsState.confirm, text="Bekor qilish")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(text="Bekor qilindi")
    await state.finish()
