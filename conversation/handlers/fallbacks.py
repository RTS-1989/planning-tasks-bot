import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

logger = logging.getLogger(__name__)


def init_fallbacks(dp: Dispatcher):
    @dp.message_handler(lambda message: True)
    async def fallback(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            logger.info(message.text, extra=data)
