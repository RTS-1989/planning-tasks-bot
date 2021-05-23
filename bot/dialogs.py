from dataclasses import dataclass


@dataclass(frozen=True)
class Messages:
    test: str = 'Привет, {name}!'
    services: str = 'Сервисы'
    choose_services: str = 'Выберите интересующий вас сервис:'
    help: str = 'Помощь'
    help_message: str = 'Данное приложение выполняет следующие команды: \n' \
                        '/start - Начало работы с ботом.'
    main: str = "Что будем делать?"
    btn_back: str = "<- Назад"
    btn_forward: str = "Вперед ->"


msg = Messages()
