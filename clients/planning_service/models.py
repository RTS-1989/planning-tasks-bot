from typing import Optional, List


class FlatPlan:
    __slots__ = 'id', 'task_name', 'category', 'countable_value', 'bot_user_id', 'date', 'done'

    def __init__(self, identifier: int, task_name: str, category: str, countable_value: int,
                 bot_user_id: int, date: str, done: bool):
        self.id = identifier
        self.task_name = task_name
        self.category = category,
        self.countable_value = countable_value
        self.bot_user_id = bot_user_id
        self.date = date
        self.done = done


class FlatBotUser:
    __slots__ = 'id', 'surname', 'first_name', 'patronymic', 'is_active', 'email', 'full_name', 'birthday'

    def __init__(self, identifier: int, surname: str, first_name: str, patronymic: Optional[str], is_active: bool,
                 email: Optional[str], full_name: str, birthday: Optional[str]):
        self.id = identifier
        self.surname = surname
        self.first_name = first_name
        self.patronymic = patronymic
        self.is_active = is_active
        self.email = email
        self.full_name = full_name
        self.birthday = birthday


class FlatTelegram:
    __slots__ = 'id', 'bot_user_id', 'username', 'user_id', 'is_active'

    def __init__(self, identifier: int, bot_user_id: int, username: str, user_id: int, is_active: bool):
        self.id = identifier
        self.bot_user_id = bot_user_id
        self.username = username
        self.user_id = user_id
        self.is_active = is_active


class FlatPhone:
    __slots__ = 'id', 'bot_user_id', 'national', 'international', 'is_active'

    def __init__(self, identifier: int, bot_user_id: int, national: str, international: str, is_active: bool):
        self.id = identifier
        self.bot_user_id = bot_user_id
        self.national = national
        self.international = international
        self.is_active = is_active


class BotUser(FlatBotUser):
    __slots__ = 'id', 'surname', 'first_name', 'patronymic', 'is_active', 'email', 'full_name', 'birthday', 'phones', \
                'telegrams'

    def __init__(self, identifier: int, surname: str, first_name: str, patronymic: Optional[str], is_active: bool,
                 email: Optional[str], full_name: str, birthday: Optional[str], phones: List[FlatPhone],
                 telegrams: List[FlatTelegram]):
        super().__init__(identifier, surname, first_name, patronymic, is_active, email, full_name, birthday)
        self.phones = phones
        self.telegrams = telegrams


class Telegram(FlatTelegram):
    __slots__ = 'id', 'bot_user_id', 'username', 'user_id', 'is_active', 'bot_user'

    def __init__(self, identifier: int, bot_user_id: int, username: str, user_id: int, is_active: bool,
                 bot_user: FlatBotUser):
        super().__init__(identifier, bot_user_id, username, user_id, is_active)
        self.bot_user = bot_user


class Plan(FlatPlan):
    __slots__ = 'id', 'task_name', 'category', 'countable_value', 'bot_user_id', 'bot_user', 'date', 'done'

    def __init__(self, identifier: int, task_name: str, category: str, countable_value: int, bot_user_id: int,
                 date: str, done: bool, bot_user: FlatBotUser):
        super().__init__(identifier, task_name, category, countable_value, bot_user_id, date, done)
        self.bot_user = bot_user


class Phone(FlatPhone):
    __slots__ = 'id', 'bot_user_id', 'national', 'international', 'is_active', 'bot_user'

    def __init__(self, identifier: int, bot_user_id: int, national: str, international: str, is_active: bool,
                 bot_user: FlatBotUser):
        super().__init__(identifier, bot_user_id, national, international, is_active)
        self.bot_user = bot_user
