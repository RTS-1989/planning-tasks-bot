from aiogram.utils.executor import Executor

from bot.main import init_bot, start_bot
from conversation.main import init_handlers
from clients.planning_service.service import PlanningService
from environment import init_environment
from redis import init_redis
from repositories.redis_repository import RedisRepository


def start_app():
    environment = init_environment()

    bot, dispatcher = init_bot(environment)

    executor = Executor(dispatcher)

    async def on_startup(*_, **__):

        planning_service = PlanningService(environment)

        redis = await init_redis(environment)
        redis_repository = RedisRepository(redis)

        init_handlers(dp=dispatcher, planning_service=planning_service, redis_repository=redis_repository)

    async def on_shutdown(*_, **__):
        pass

    executor.on_startup(on_startup)
    executor.on_shutdown(on_shutdown)
    start_bot(executor=executor, environment=environment)


if __name__ == '__main__':
    start_app()
