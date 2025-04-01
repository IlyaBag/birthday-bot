from aiogram import Router, F
from aiogram.types import Message

from utils.cli_commands import get_raspberry_cpu_temp


router = Router()

@router.message(F.text == 'temp')
async def check_cpu_temp(msg: Message) -> None:
    temp = get_raspberry_cpu_temp()
    await msg.answer(temp)
