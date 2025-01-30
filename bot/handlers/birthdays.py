from aiogram import Router, F
from aiogram.types import Message

from utils.date import fetch_birthday_person


router = Router()


@router.message(F.text == 'Сегодня')
async def get_today_birthday(msg: Message) -> None:
    person = fetch_birthday_person()
    await msg.answer(person)


@router.message(F.text == 'Другой день')
async def get_another_day_birthday(msg: Message) -> None:
    await msg.answer('Какая дата тебя интересует?\n'
                     'Напиши число и месяц в виде ДД.ММ, например 29.02')


date_regex = r'([0][1-9]|[12][0-9]|[3][01])\.([0][1-9]|[1][0-2])'

@router.message(F.text.regexp(date_regex))
async def get_certain_day_birthday(msg: Message) -> None:
    date = msg.text or ''  # empty string replaces 'None' in msg.text for mypy
    person = fetch_birthday_person(date)
    await msg.answer(person)


@router.message(F.text == 'Ближайший')
async def get_next_birthday(msg: Message) -> None:
    await msg.answer('Извини, так я пока не умею делать')
