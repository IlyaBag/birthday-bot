import asyncio
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.chat_action import ChatActionSender

from create_bot import bot
from keyboards.birthday_kb import main_menu_kb
from repo.json_storage import get_birthday_by_person
from utils.date import fetch_birthday_person


class Search(StatesGroup):
    query = State()


router = Router()


@router.message(F.text == '🔎 Поиск')
async def find_birthday_or_person(msg: Message, state: FSMContext) -> None:
    await state.clear()
    answer = await msg.answer(
        'Давай поищем. Искать можно по имени или по дате.\n' \
        'Напиши фамилию или имя человека, либо число и месяц в виде ДД.ММ, ' \
        'например 29.02',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_data({'del_msg_ids': (msg.message_id, answer.message_id)})
    await state.set_state(Search.query)


date_regex = r'([0][1-9]|[12][0-9]|[3][01])\.([0][1-9]|[1][0-2])'

@router.message(F.text.regexp(date_regex), Search.query)
async def find_birthday_by_date(msg: Message, state: FSMContext) -> None:
    data = await state.get_data()
    date = msg.text
    person = fetch_birthday_person(date)
    await bot.delete_messages(chat_id=msg.chat.id,
                              message_ids=data.get('del_msg_ids'))
    await msg.answer(person,
                     reply_markup=main_menu_kb(user_id=msg.from_user.id))
    await state.clear()


@router.message(F.text, Search.query)
async def find_birthday_by_name(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)

    data = await state.get_data()
    async with ChatActionSender.typing(bot=bot, chat_id=msg.chat.id):
        await asyncio.sleep(1)
        birthday = get_birthday_by_person(data.get('name'))
        if not birthday:
            birthday = 'Извините, такого имени нет в моих записях 😞'
    await bot.delete_messages(chat_id=msg.chat.id,
                              message_ids=data.get('del_msg_ids'))
    await msg.answer(birthday,
                     reply_markup=main_menu_kb(user_id=msg.from_user.id))
    await state.clear()
