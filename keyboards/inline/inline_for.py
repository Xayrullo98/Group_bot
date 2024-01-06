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
