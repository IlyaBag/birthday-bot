from datetime import date, timedelta
from aiogram import Router, F
from aiogram.types import Message

from repo.json_storage import get_all_birthdays
from utils.date import fetch_birthday_person


router = Router()


@router.message(F.text == 'Сегодня')
async def get_today_birthday(msg: Message) -> None:
    person = fetch_birthday_person()
    await msg.answer(person)


@router.message(F.text == 'Ближайший')
async def get_next_birthday(msg: Message) -> None:
    date_ = date.today()
    all_birthdays = get_all_birthdays()
    birthday_person = None
    while not birthday_person:
        date_ += timedelta(days=1)
        date_str = f'{date_:%d.%m}'
        birthday_person = all_birthdays.get(date_str)
    await msg.answer(f'{date_str}: {birthday_person}')
