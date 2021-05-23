from aiogram.dispatcher.filters.state import StatesGroup, State


class MessageInfo(StatesGroup):
    country = State()
