from typing import Generator, List, Union, Optional
import datetime
import httpx
from aiogram.utils.exceptions import ValidationError
from httpx import Auth, Request, Response

from environment import Environment

from clients.planning_service.presenters import PlanPresenter
from clients.planning_service.response import PlanResponse, PlanListSuccessResponse, PlanCreateSuccessResponse
from clients.planning_service.models import Telegram, Phone, Plan


class TokenAuthentication(Auth):

    def __init__(self, token: str):
        self.token = token

    def auth_flow(self, request: Request) -> Generator[Request, Response, None]:
        request.headers['Authorization'] = f"Token {self.token}"
        yield request


class PlanningService:

    def __init__(self, env: Environment):
        self.client = httpx.AsyncClient(auth=TokenAuthentication(token=env.planning_bot_token),
                                        base_url=env.planning_bot_host)
        self.presenter = PlanPresenter()

    @staticmethod
    def _clear_params(params: dict) -> dict:
        return {k: v for k, v in params.items() if v is not None}

    async def create_telegram(self, bot_user_id: int,
                              telegram_user_id: int,
                              telegram_username: str):
        response = await self.client.post('/api/v1/telegrams/', json={
            'bot_user_id': bot_user_id,
            'user_id': telegram_user_id,
            'username': telegram_username
        })

        data: dict = response.json()

        if response.status_code == 201:
            self.presenter.parse_telegram(data)
        else:
            return data

    async def send_planning_task(self, task_name: str, deadline: str,
                                 bot_user_id: int,
                                 countable_value: int = None,
                                 category: str = None,
                                 done: bool = False) -> Union[PlanCreateSuccessResponse[Plan], PlanResponse]:
        date_format = datetime.datetime.strptime(deadline, "%d-%m-%Y").date()
        response = await self.client.post("/api/v1/plans/", json={
            "task_name": task_name,
            "category": category,
            "countable_value": countable_value,
            "bot_user_id": bot_user_id,
            "date": str(date_format),
            "done": done
        })

        print(response.status_code)
        data: dict = response.json()
        print(data)

        if response.status_code == 201:
            return PlanCreateSuccessResponse(status=response.status_code,
                                             item=self.presenter.parse_plan(data))
        else:
            return PlanResponse(status=response.status_code)

    async def get_planning_task(self, search: int, page_size: int = 100, page: int = 1):
        response = await self.client.get('/api/v1/plans/', params={
            'search': search,
            'page_size': page_size,
            'page': page
        })

        data: dict = response.json()

        if response.status_code == 200:
            return data
        else:
            return data

    async def telegrams(self, user_id: int = None, bot_user_id: int = None) -> Union[List[Telegram], dict]:
        response = await self.client.get('/api/v1/telegrams/', params=self._clear_params({
            'user_id': user_id,
            'bot_user_id': bot_user_id
        }))

        data: dict = response.json()

        if response.status_code == 200:
            return [self.presenter.parse_telegram(i) for i in data.get("results", [])]
        else:
            return data

    async def phones(self, e164: str = None, search: str = None, bot_user_is_active: bool = True) -> \
            Union[List[Phone], dict]:
        response = await self.client.get("/api/v1/phones/", params=self._clear_params({
            "e164": e164,
            "search": search,
            "is_active": bot_user_is_active
        }))

        data: dict = response.json()

        if response.status_code == 200:
            return [self.presenter.parse_phone(i) for i in data.get("results", [])]
        else:
            return data
