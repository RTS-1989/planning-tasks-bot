import datetime

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import calendar

from my_calendar.dialogs import msg
from my_calendar.date_config import MONTHS

CALENDAR_MAIN_KB = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton(msg.test))

YEAR_DEFAULT = datetime.date.today().year


def get_month_days_number(month: int, year: int = YEAR_DEFAULT) -> int:
    _, month_days = calendar.monthrange(year, month)
    return month_days


def choose_month_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    months_keys = list(MONTHS.keys())
    for month_id in months_keys:
        kb.add(
            InlineKeyboardButton(
                f'{month_id}. {MONTHS[month_id][0]}',
                callback_data=f'choose_month_#{month_id}'
            )
        )
    return kb


def days_of_month_keyboard(month: int) -> InlineKeyboardMarkup:

    kb = InlineKeyboardMarkup(row_width=7)
    days_in_month = get_month_days_number(month)
    list_of_days_in_month = [str(item + 1) for item in range(days_in_month)]

    row = []
    for day in list_of_days_in_month:
        row.append(InlineKeyboardButton(
            day, callback_data=f'choose_date_#{day}'))

    row_1, row_2, row_3 = row[0:10], row[10:20], row[20:30] if len(row[20:30]) == 10 else \
        row[20:29] if len(row[20:29]) == 9 else row[20:28]

    for number, item in enumerate(row_1):
        print(f'{number}. {item}')

    kb.add(row_1[0], row_1[1], row_1[2], row_1[3], row_1[4], row_1[5], row_1[6], row_1[7], row_1[8], row_1[9])
    kb.add(row_2[0], row_2[1], row_2[2], row_2[3], row_2[4], row_2[5], row_2[6], row_2[7], row_2[8], row_2[9])
    kb.add(row_3[0], row_3[1], row_3[2], row_3[3], row_3[4], row_3[5], row_3[6], row_3[7], row_3[8], row_3[9]) if \
        len(row_3) == 10 else kb.add(row_3[0], row_3[1], row_3[2], row_3[3], row_3[4], row_3[5], row_3[6], row_3[7],
                                     row_3[8], '') if len(row_3) == 9 else \
        kb.add(row_3[0], row_3[1], row_3[2], row_3[3], row_3[4], row_3[5], row_3[6], row_3[7])
    if row.index(row[-1]) == 30:
        kb.add(row[-1])
    return kb
