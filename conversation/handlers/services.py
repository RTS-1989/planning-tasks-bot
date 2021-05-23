from aiogram import types
from aiogram.dispatcher import Dispatcher

from bot.dialogs import msg
from bot.service import MAIN_KB
from my_calendar.keyboard import CALENDAR_MAIN_KB
from bot.service import services_kb, countries_kb
from planning.keyboard import planning_keyboard
from config import SERVICES

services_kbs = {
    '1': planning_keyboard,
    '2': '',
    '3': countries_kb,
    '4': '',
    '5': '',
    '6': '',
    '7': '',
    '8': ''
}


def init_services_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def start_handler(message: types.Message):
        user_name = message.from_user.first_name
        await message.answer(msg.test.format(name=user_name), reply_markup=MAIN_KB)

    @dp.message_handler(commands=['help'])
    async def help_handler(message: types.Message):
        await message.answer(msg.help_message, reply_markup=MAIN_KB)

    @dp.message_handler(lambda message: message.text == msg.services)
    async def get_services(message: types.Message):
        await message.answer(msg.choose_services, reply_markup=services_kb())

    @dp.callback_query_handler(lambda c: c.data.startswith('edit_config'))
    async def set_or_update_config(callback_query: types.CallbackQuery = None, offset=0):

        if callback_query is not None:
            offset = int(callback_query.data.split('#')[-1])

        if offset == 0:
            await callback_query.message.edit_reply_markup(
                reply_markup=services_kb()
            )
        else:
            await callback_query.message.edit_reply_markup(
                reply_markup=services_kb(offset)
            )

    @dp.callback_query_handler(lambda c: c.data.startswith('choose_service'))
    async def choose_service(callback_query: types.CallbackQuery = None):
        service_id = 0
        if callback_query:
            service_id = callback_query.data.split('#')[-1]
        print(service_id)

        for s_id in SERVICES.keys():
            print(s_id)
            if s_id == service_id:
                await callback_query.message.edit_reply_markup(reply_markup=services_kbs[s_id]())
                break

    # @dp.callback_query_handler(lambda c: c.data == 'main_window')
    # async def show_main_window(callback_query: types.CallbackQuery):
    #     """Главный экран"""
    #     await callback_query.answer()
    #     await bot.send_message(callback_query.from_user.id, msg.main, reply_markup=MAIN_KB)
