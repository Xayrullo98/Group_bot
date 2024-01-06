from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from filters.guruh_uchun import Guruh
from loader import dp, bot
from data.config import  guruh
from data.check import checking


@dp.message_handler(Guruh())
async def bot_start(message: types.Message):
    text = message.text
    chat_id = message.chat.id
    ism = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    full_text = f"<strong> {ism} </strong> \n" + str(text)
    check = await checking(user_id=user_id, kanal_link=guruh[0])
    guruh_link = message.chat.username
    if check:
        pass
    else:
        if 'оламиз' in text \
                or 'Оламиз' in text \
                or "ОЛАМИЗ" in text \
                or "olamiz" in text \
                or "Olamiz" in text \
                or "OLAMIZ" in text \
                or "yuramiz" in text\
                or "Yuramiz" in text\
                or "YURAMIZ" in text\
                or "юрамиз" in text\
                or "Юрамиз" in text\
                or "ЮРАМИЗ" in text:
            await bot.delete_message(chat_id=chat_id, message_id=message.message_id, )
        elif '93' in text \
                or '94' in text \
                or "90" in text \
                or "91" in text \
                or "33" in text \
                or "88" in text \
                or "95" in text \
                or "97" in text \
                or "98" in text \
                or "99" in text \
                or "71" in text \
                or "78" in text:
            try:
                await bot.forward_message(chat_id=guruh[0], from_chat_id=f'{guruh_link}',
                                          message_id=message.message_id)
                await message.answer(
                    f"XURMATLI MIJOZ {message.from_user.full_name.upper()}!. GRUPPAMIZ ORQALI  7 MARTA TAKSI ZAKAZ BERING 8 CHISI MUTLOQ BEPUL")
                await bot.delete_message(chat_id=chat_id, message_id=message.message_id, )
            except Exception as e:
                if 'Chat not found'!=str(e):
                    await bot.send_message(chat_id='6570924683',text=f"{e}")
                if username:
                    await bot.send_message(chat_id=guruh[0], text=full_text,
                                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(text="МИЖОЗ", url=f"https://t.me/{username}"),
                                                   InlineKeyboardButton(text="ГУРУХ", url=f"https://t.me/{guruh_link}"),
                                               ]
                                           ]
                                           )
                                           )
                else:
                    await bot.send_message(chat_id=guruh[0], text=full_text,
                                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                               [

                                                   InlineKeyboardButton(text="ГУРУХ", url=f"https://t.me/{guruh_link}"),
                                               ]
                                           ]
                                           )
                                           )
                await message.answer(
                    f"XURMATLI MIJOZ {message.from_user.full_name.upper()}!. GRUPPAMIZ ORQALI  7 MARTA TAKSI ZAKAZ BERING 8 CHISI MUTLOQ BEPUL")
                await bot.delete_message(chat_id=chat_id, message_id=message.message_id, )
        else:

            try:
                await bot.forward_message(chat_id=guruh[0], from_chat_id=f'{guruh_link}',
                                          message_id=message.message_id)
                await message.answer(
                    f"XURMATLI MIJOZ  {message.from_user.full_name}   TEL RAQAMINGIZNI QOLDIRING XAYDOVCHILAR SIZ BILAN BOG'LANISHADI.\n\n\n BIZNI TANLAGANIZ UCHUN RAXMAT")
                await bot.delete_message(chat_id=chat_id, message_id=message.message_id, )
            except Exception as e:
                if 'Chat not found'!=str(e):
                    await bot.send_message(chat_id='6570924683',text=f"{e}")
                if username:
                    await bot.send_message(chat_id=guruh[0], text=full_text,
                                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                               [
                                                   InlineKeyboardButton(text="МИЖОЗ", url=f"https://t.me/{username}"),
                                                   InlineKeyboardButton(text="ГУРУХ", url=f"https://t.me/{guruh_link}"),
                                               ]
                                           ]
                                           )
                                           )
                else:
                    await bot.send_message(chat_id=guruh[0], text=full_text,
                                           reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                               [

                                                   InlineKeyboardButton(text="ГУРУХ", url=f"https://t.me/{guruh_link}"),
                                               ]
                                           ]
                                           )
                                           )
                await message.answer(
                    f"XURMATLI MIJOZ  {message.from_user.full_name}   TEL RAQAMINGIZNI QOLDIRING XAYDOVCHILAR SIZ BILAN BOG'LANISHADI.\n\n\n BIZNI TANLAGANIZ UCHUN RAXMAT")
                await bot.delete_message(chat_id=chat_id, message_id=message.message_id, )
