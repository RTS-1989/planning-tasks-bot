from aiogram.dispatcher import Dispatcher
from aiogram import types

from conversation.constants import BACK_TO_MENU_BUTTON
from nasa_api.nasa_api_dialogs import nasa_api_msg
from nasa_api.service import NasaImageOfTheDay


def init_nasa_api_handler(dp: Dispatcher, nasa_api_service: NasaImageOfTheDay):
    @dp.callback_query_handler(lambda c: c.data.startswith('chosen_nasa_api'))
    async def get_nasa_photo(callback_query: types.CallbackQuery = None):
        nasa_photo_text = nasa_api_msg.send_photo_of_the_day
        nasa_photo_url = nasa_api_service.get_image_of_the_day_url()
        chat_id = callback_query.message.chat.id
        await dp.bot.send_message(chat_id=chat_id, text=nasa_photo_text, reply_markup=BACK_TO_MENU_BUTTON)
        await dp.bot.send_photo(chat_id=chat_id, photo=nasa_photo_url)
