from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from create_bot import admins


BTN_TODAY = '🎉 Сегодня'
BTN_NEAREST = '⏳ Ближайший'
BTN_SEARCH = '🔎 Поиск'
BTN_LOGS = 'logs'
BTN_TEMP = 'temp'


def main_menu_kb(user_id: int) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=BTN_TODAY)
    keyboard.button(text=BTN_NEAREST)
    keyboard.button(text=BTN_SEARCH)
    if user_id in admins:
        keyboard.button(text=BTN_LOGS)
        keyboard.button(text=BTN_TEMP)
    keyboard.adjust(2, 1, 2)
    return keyboard.as_markup(resize_keyboard=True,
                              input_field_placeholder='Нажми на кнопку')
