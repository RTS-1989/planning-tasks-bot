import datetime

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from planning.planning_config import PLANNING_KEYBOARD_TASKS


def planning_keyboard():
    kb = InlineKeyboardMarkup()
    services_keys_list = list(PLANNING_KEYBOARD_TASKS.keys())

    for key in services_keys_list:
        kb.add(
            InlineKeyboardButton(
                f'{key}. {PLANNING_KEYBOARD_TASKS[key]}',
                callback_data=f'planning_kb_#{key}'
            )
        )

    return kb


def planning_is_countable_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton('Да', callback_data='yes'),
        InlineKeyboardButton('Нет', callback_data='no')
    )

    return kb
