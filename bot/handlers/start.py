from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.birthday_kb import main_menu_kb
from utils.users import get_all_users_ids, temporary_save_new_user


router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message) -> None:
    user = msg.from_user
    users = get_all_users_ids()
    if user.id not in users:
        temporary_save_new_user(user)
    name = user.first_name or 'друг'
    await msg.answer(f'Привет, {name}!', reply_markup=main_menu_kb())
