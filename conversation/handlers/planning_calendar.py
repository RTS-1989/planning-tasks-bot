from aiogram.dispatcher import Dispatcher
from aiogram import types

from my_calendar.date_config import MONTHS
from my_calendar.keyboard import days_of_month_keyboard


def init_planning_calendar(dp: Dispatcher):
    @dp.callback_query_handler(lambda c: c.data.startswith('choose_month'))
    async def choose_month(callback: types.CallbackQuery):
        month_id = ''
        if callback.data:
            month_id = callback.data.split('#')[-1]
            print(month_id)
        print(month_id)
        for m_id in MONTHS.keys():
            if month_id == m_id:
                await callback.message.edit_reply_markup(reply_markup=days_of_month_keyboard(int(month_id)))
