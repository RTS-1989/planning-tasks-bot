from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from clients.planning_service.service import PlanningService
from bot.service import services_kb, MAIN_KB
from conversation.constants import SHARE_PHONE_REPLY
from conversation.states.registration import RegistrationState


def init_registration_handlers(dp: Dispatcher, planning_service: PlanningService):
    @dp.message_handler(lambda message: message.bot_user_id is None, content_types=ContentType.CONTACT,
                        state=RegistrationState.registration)
    async def registration_phone_contact_handler(message: types.Message, state: FSMContext):
        phones = await planning_service.phones(search=message.contact.phone_number)
        if len(phones) > 1:
            full_names = ", ".join([p.bot_user.first_name for p in phones])
            await message.answer(f"Найдено много сотрудников: {full_names}")
        elif len(phones) <= 0:
            await message.answer(f"Не удалось найти ни одного сотрудника")
        else:
            bot_user = phones[0].bot_user
            telegrams = await planning_service.telegrams(user_id=message.from_user.id)
            if len(telegrams) > 0:
                await message.answer(f"Вы уже зарегистрированы как {bot_user.full_name}", reply_markup=MAIN_KB)
            else:
                await planning_service.create_telegram(bot_user_id=bot_user.id,
                                                       telegram_user_id=message.from_user.id,
                                                       telegram_username=message.from_user.username)
                await message.answer(f"Вы успешно зарегистрировались как {bot_user.full_name}", reply_markup=MAIN_KB)
            await state.finish()

    @dp.message_handler(lambda message: message.bot_user_id is None, state=RegistrationState.registration)
    async def registration_phone_handler(message: types.Message):
        if message.contact is None:
            await message.answer('Нужно поделиться контактом с помощью следующей кнопки',
                                 reply_markup=SHARE_PHONE_REPLY)
        elif message.is_forward():
            await message.answer("Нельзя пересылать контакты", reply_markup=SHARE_PHONE_REPLY)
