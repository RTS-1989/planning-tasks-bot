from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import types

from bot.service import regions_kb
from countries_app.countries import get_country_by_message, get_countries_by_region
from conversation.states.country_search import MessageInfo
from countries_app.countries_dialogs import countries_msg
from countries_app.config_countries import REGIONS


def init_country_by_text_search(dp: Dispatcher):
    @dp.callback_query_handler(lambda c: c.data.startswith('chosen_country_service'))
    async def choose_countries_in_region(callback_query: types.CallbackQuery = None):
        country_service_id = 0
        if callback_query:
            country_service_id = callback_query.data.split('#')[-1]

        if country_service_id == '1':
            await callback_query.message.edit_reply_markup(reply_markup=regions_kb())
        elif country_service_id == '2':
            await callback_query.message.answer(countries_msg.write_country)
            await MessageInfo.country.set()

    @dp.message_handler(state=MessageInfo.country)
    async def get_country_info(message: types.Message, state: FSMContext):
        print('get_country_info')
        await state.update_data(country_name=message.text)
        user_data = await state.get_data()
        country = user_data.get('country_name')
        country_info = '\n'.join([f'{k}: {v}' for k, v in get_country_by_message(country).items()])
        await message.answer(country_info)
        await state.finish()

    @dp.callback_query_handler(lambda c: c.data.startswith('chosen_region'))
    async def get_region_info(callback_query: types.CallbackQuery = None):
        region_id = ''
        if callback_query:
            region_id = callback_query.data.split('#')[-1]
        region = REGIONS[region_id][0]
        print(region)
        region_countries_info = '\n'.join([f'{country}' for country in get_countries_by_region(region)])
        await callback_query.message.answer(region_countries_info)
