from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Сегодня')
    keyboard.button(text='Ближайший')
    keyboard.button(text='🔎 Поиск')
    keyboard.adjust(2, 1)
    return keyboard.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Нажми на кнопку'
    )
