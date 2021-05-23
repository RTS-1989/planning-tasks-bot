from environs import Env


class Environment:
    def __init__(self, _env: Env):
        self.telegram_token = _env.str('TELEGRAM_BOT_TOKEN', '')
        self.telegram_webhook = _env.bool("TELEGRAM_WEBHOOK", "False")
        self.telegram_webhook_path = _env.str("TELEGRAM_WEBHOOK_PATH", f"/hook/")
        self.telegram_webhook_host = _env.str("TELEGRAM_WEBHOOK_HOST") if self.telegram_webhook else None

        self.redis_host = _env.str('REDIS_HOST', 'localhost')
        self.redis_port = _env.str('REDIS_PORT', '6379')
        self.redis_password = _env.str('REDIS_PASSWORD', '')

        self.planning_bot_host = _env.str('PLANNING_BOT_HOST', '')
        self.planning_bot_token = _env.str('PLANNING_BOT_TOKEN', '')

        self.yandex_rasp_token = _env.str('YANDEX_RASP_TOKEN', '')

    @property
    def redis_uri(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"


def init_environment() -> Environment:
    env = Env()
    env.read_env()
    return Environment(_env=env)
