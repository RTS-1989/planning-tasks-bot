from aioredis import Redis


ENCODING = 'utf-8'


class RedisRepository:
    def __init__(self, redis: Redis):
        self.redis = redis

    @staticmethod
    def _get_bot_user_id_by_telegram_id_key(telegram_id: int) -> str:
        return f"bot-user-id-by-telegram-id-{telegram_id}"

    async def set_bot_user_id_by_telegram_id(self, telegram_id: int, bot_user_id: int):
        key = self._get_bot_user_id_by_telegram_id_key(telegram_id=telegram_id)
        await self.redis.set(key=key, value=bot_user_id, expire=3600)

    async def get_bot_user_id_by_telegram_id(self, telegram_id: int) -> int:
        key = self._get_bot_user_id_by_telegram_id_key(telegram_id=telegram_id)
        return await self.redis.get(key=key, encoding=ENCODING)
