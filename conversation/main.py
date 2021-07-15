from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from conversation.handlers.common import init_common_handlers
from conversation.handlers.country_search import init_country_by_text_search
from conversation.handlers.planning_services import init_planning_tasks
from conversation.handlers.services import init_services_handlers
from conversation.handlers.fallbacks import init_fallbacks
from conversation.handlers.planning_calendar import init_planning_calendar
from conversation.handlers.registration import init_registration_handlers
from conversation.handlers.nasa_api_handler import init_nasa_api_handler
from conversation.middlewares.authentication import AuthenticationMiddleware
from clients.planning_service.service import PlanningService
from repositories.redis_repository import RedisRepository
from nasa_api.service import NasaImageOfTheDay


def init_handlers(dp: Dispatcher, planning_service: PlanningService, redis_repository: RedisRepository,
                  nasa_image: NasaImageOfTheDay):
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(AuthenticationMiddleware(planning_service=planning_service,
                                                 redis_repository=redis_repository))

    init_common_handlers(dp, planning_service)
    init_registration_handlers(dp, planning_service)
    init_services_handlers(dp),
    init_country_by_text_search(dp)
    init_planning_tasks(dp, planning_service)
    init_nasa_api_handler(dp, nasa_image)
    init_fallbacks(dp)
    init_planning_calendar(dp)
