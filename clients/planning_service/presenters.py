from typing import TypeVar, Type

from clients.planning_service.models import FlatPlan, FlatBotUser, FlatTelegram, FlatPhone, Telegram, Plan, Phone

T = TypeVar('T')


class PlanPresenter:

    @staticmethod
    def parse_flat_plan(data: dict, cls: Type[T] = FlatPlan, additional_fields: dict = None) -> T:
        if data is None:
            return None
        if additional_fields is None:
            additional_fields = {}
        return cls(
            identifier=data.get('identifier'),
            task_name=data.get('task_name'),
            category=data.get('category'),
            countable_value=data.get('countable_value'),
            bot_user_id=data.get('bot_user_id'),
            date=data.get('date'),
            done=data.get('done'),
            **additional_fields
        )

    @staticmethod
    def parse_flat_bot_user(data: dict, cls: Type[T] = FlatBotUser, additional_fields: dict = None):
        if data is None:
            return None
        if additional_fields is None:
            additional_fields = {}
        return cls(
            identifier=data.get('id'),
            surname=data.get('surname'),
            first_name=data.get('first_name'),
            patronymic=data.get('patronymic'),
            is_active=data.get('is_active'),
            email=data.get('email'),
            full_name=data.get('full_name'),
            birthday=data.get('birthday'),
            **additional_fields
        )

    @staticmethod
    def parse_flat_telegram(data: dict, cls: Type[T] = FlatTelegram, additional_fields: dict = None):
        if data is None:
            return None
        if additional_fields is None:
            additional_fields = {}
        return cls(
            identifier=data.get('id'),
            username=data.get('first_name'),
            bot_user_id=data.get('bot_user_id'),
            user_id=data.get('user_id'),
            is_active=data.get('is_active'),
            **additional_fields
        )

    @staticmethod
    def parse_flat_phone(data: dict, cls: Type[T] = FlatPhone, additional_fields: dict = None):
        if data is None:
            return None
        if additional_fields is None:
            additional_fields = {}
        return cls(
            identifier=data.get('identifier'),
            bot_user_id=data.get('bot_user_id'),
            national=data.get('national'),
            international=data.get('international'),
            is_active=data.get('is_active'),
            **additional_fields
        )

    def parse_plan(self, data: dict) -> Plan:
        return self.parse_flat_plan(data, Plan, {"bot_user": self.parse_flat_bot_user(data.get('bot_user'))})

    def parse_telegram(self, data: dict) -> Telegram:
        return self.parse_flat_telegram(data, Telegram, {"bot_user": self.parse_flat_bot_user(data.get('bot_user'))})

    def parse_phone(self, data: dict) -> Phone:
        return self.parse_flat_phone(data, Phone, {"bot_user": self.parse_flat_bot_user(data.get('bot_user'))})
