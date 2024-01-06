from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def button(link, username=None):
    if username:
        inline_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Mijoz", url=f"https://t.me/{username}"),
                    InlineKeyboardButton(text="Guruh", url=f"{link}"),
                ]
            ]
        )
        return inline_button
    else:
        inline_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [

                    InlineKeyboardButton(text="Guruh", url=f"{link}"),
                ]
            ]
        )
        return inline_button


async def ads_button(channels):
    inline = []
    for i in channels:
        inline_button=[]
        inline_button.append(
            InlineKeyboardButton(text=f"{i}", callback_data=f"{i}")
        )
        inline.append(inline_button)
    inline.append([InlineKeyboardButton(text="Barchasi",callback_data="all")])
    inline.append([InlineKeyboardButton(text="Tasdiqlash",callback_data="confirm")])
    return InlineKeyboardMarkup(inline_keyboard=inline)
