from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text='Сегодня')
    keyboard.button(text='Другой день')
    keyboard.button(text='Ближайший')
    keyboard.adjust(1)
    return keyboard.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Интересуют дни рождения?'
    )
