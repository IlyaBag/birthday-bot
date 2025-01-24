from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.birthday_kb import main_menu_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message) -> None:
    user = msg.from_user
    name = user.first_name if user else 'друг'
    await msg.answer(f'Привет, {name}!', reply_markup=main_menu_kb())
