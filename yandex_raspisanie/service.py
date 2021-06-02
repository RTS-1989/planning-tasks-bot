import httpx
import requests

from environment import Environment
from clients.planning_service.service import TokenAuthentication


class YandexScheduleService:

    def __init__(self, env: Environment):
        self.client = httpx.AsyncClient(auth=TokenAuthentication(token=env.yandex_rasp_token),
                                        base_url=env.yandex_rasp_url)

    @staticmethod
    def _clear_params(params: dict) -> dict:
        return {k: v for k, v in params.items() if v is not None}

    async def get_trip(self, go_from: str, go_to: str):
        response = await self.client.get('/v3.0/search/', params={
            'from': go_from,
            'to': go_to
        })

        data: dict = response.json()

        if response.status_code == 200:
            return data



