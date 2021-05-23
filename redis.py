import aioredis
from aioredis import Redis

from environment import Environment


async def init_redis(environment: Environment) -> Redis:
    return await aioredis.create_redis_pool(environment.redis_uri)
