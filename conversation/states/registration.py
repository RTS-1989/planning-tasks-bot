from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationState(StatesGroup):
    registration = State()
