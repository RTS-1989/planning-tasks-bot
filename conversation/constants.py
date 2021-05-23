from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

BACK_TO_MENU_TEXT: str = 'Вернуться в меню'


BACK_TO_MENU_BUTTON = ReplyKeyboardMarkup([[KeyboardButton(text=BACK_TO_MENU_TEXT)]], resize_keyboard=True)
REMOVE_INLINE_KEYBOARD_REPLY = InlineKeyboardMarkup(inline_keyboard=[])
SHARE_PHONE_REPLY = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Зарегистрироваться",
                                                                  request_contact=True)]], resize_keyboard=True)
