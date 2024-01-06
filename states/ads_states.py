from aiogram.dispatcher.filters.state import State,StatesGroup


class AdsState(StatesGroup):
    post = State()
    channel = State()
    send = State()
    confirm = State()
