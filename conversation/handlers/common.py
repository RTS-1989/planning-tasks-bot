import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from clients.planning_service.service import PlanningService
from conversation.constants import SHARE_PHONE_REPLY, BACK_TO_MENU_TEXT
from bot.service import MAIN_KB
from conversation.states.registration import RegistrationState


logger = logging.getLogger(__name__)


def init_common_handlers(dp: Dispatcher, planning_service: PlanningService):
    async def _start_handler(message: types.Message, state: FSMContext):
        await state.finish()
        telegrams = await planning_service.telegrams(user_id=message.from_user.id)
        if len(telegrams) <= 0:
            await RegistrationState.registration.set()
            await message.answer("Приветствую тебя, для начала тебе необходимо зарегистрироваться👇",
                                 reply_markup=SHARE_PHONE_REPLY)
        else:
            bot_user = telegrams[0].bot_user
            await message.answer(f"Приветствую {bot_user.full_name}!", reply_markup=MAIN_KB)

    @dp.message_handler(lambda message: message.text.lower() == BACK_TO_MENU_TEXT.lower(), state="*")
    async def to_menu(message: types.Message, state: FSMContext):
        await _start_handler(message, state)

    @dp.message_handler(state="*", commands={"reset", "start", "menu"})
    async def reset(message: types.Message, state: FSMContext):
        await _start_handler(message, state)
