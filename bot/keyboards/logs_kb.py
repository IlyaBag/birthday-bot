from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def logs_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Удалить', callback_data='logs_del')
    kb.button(text='Оставить', callback_data='logs_leave')
    return kb.as_markup()