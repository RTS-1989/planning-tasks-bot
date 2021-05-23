import logging
from typing import Optional

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from clients.planning_service.service import PlanningService
from repositories.redis_repository import RedisRepository


class AuthenticationMiddleware(BaseMiddleware):
    def __init__(self, planning_service: PlanningService, redis_repository: RedisRepository):
        super().__init__()
        self.planning_service = planning_service
        self.redis_repository = redis_repository
        self.logger = logging.getLogger(__name__)

    async def on_process_message(self, message: types.Message, *_, **__):
        bot_user_id = await self._get_bot_user_id(message)
        setattr(message, "bot_user_id", bot_user_id)

    async def on_pre_process_message(self, message: types.Message, *_, **__):
        bot_user_id = await self._get_bot_user_id(message)
        setattr(message, "bot_user_id", bot_user_id)

    async def on_process_callback_query(self, callback_query: types.CallbackQuery, *_, **__):
        bot_user_id = await self._get_bot_user_id(callback_query.message)
        setattr(callback_query.message, "bot_user_id", bot_user_id)

    async def _get_bot_user_id(self, message: types.Message) -> Optional[int]:
        user = message.chat
        if user is None:
            return

        bot_user_id = await self.redis_repository.get_bot_user_id_by_telegram_id(user.id)
        if bot_user_id is not None:
            return bot_user_id

        telegrams = await self.planning_service.telegrams(user_id=user.id)
        if isinstance(telegrams, dict):
            return

        if len(telegrams) <= 0:
            return

        bot_user_id = telegrams[0].bot_user.id
        await self.redis_repository.set_bot_user_id_by_telegram_id(user.id, bot_user_id)
        return bot_user_id
