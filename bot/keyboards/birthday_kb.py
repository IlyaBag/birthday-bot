from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from create_bot import admins

def main_menu_kb(user_id: int) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Сегодня')
    keyboard.button(text='Ближайший')
    keyboard.button(text='🔎 Поиск')
    if user_id in admins:
        keyboard.button(text='temp')
        keyboard.button(text='logs')
    keyboard.adjust(2, 1, 2)
    return keyboard.as_markup(resize_keyboard=True,
                              input_field_placeholder='Нажми на кнопку')
