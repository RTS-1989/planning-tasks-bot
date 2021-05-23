from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from emoji import emojize

from bot.dialogs import msg
from config import SERVICES, COUNTRIES_SERVICES
from countries_app.config_countries import COUNTRIES, REGIONS

MAIN_KB = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).row(KeyboardButton(msg.services),
      KeyboardButton(msg.help)
      )


def services_kb(offset: int = 0):
    kb = InlineKeyboardMarkup()
    services_keys = list(SERVICES.keys())[0 + offset: 5 + offset]
    for service_id in services_keys:
        kb.add(
            InlineKeyboardButton(
                f'{service_id}. {SERVICES[service_id]["ru"]}',
                callback_data=f"choose_service_#{offset}_#{service_id}"
            )
        )
    if len(list(SERVICES.keys())) > 5:
        kb.row(InlineKeyboardButton(
            msg.btn_back if offset else msg.btn_forward,
            callback_data="edit_config#0" if offset else "edit_config#5")
        )
    return kb


def countries_kb():
    kb = InlineKeyboardMarkup()
    countries_keys = list(COUNTRIES_SERVICES.keys())
    for country_id in countries_keys:
        kb.add(
            InlineKeyboardButton(
                f'{country_id}. {COUNTRIES_SERVICES[country_id]}',
                callback_data=f'chosen_country_service_#{country_id}'
            )
        )
    return kb


def regions_kb():
    kb = InlineKeyboardMarkup()
    regions_keys = list(REGIONS.keys())
    for region_id in regions_keys:
        kb.add(
            InlineKeyboardButton(
                f'{region_id}. {REGIONS[region_id][0]}',
                callback_data=f'chosen_region_#{region_id}'
            )
        )
    return kb
