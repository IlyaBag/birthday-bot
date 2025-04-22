from aiogram import Router, F
from aiogram.types import Message

from utils.cli_commands import get_logs, get_raspberry_cpu_temp


router = Router()

@router.message(F.text == 'temp')
async def check_cpu_temp(msg: Message) -> None:
    temp = get_raspberry_cpu_temp()
    await msg.answer(temp)

@router.message(F.text.startswith('logs'))
async def fetch_logs(msg: Message) -> None:
    args = None
    if len(msg.text) > 5:
        args = int(str(msg.text[5:]).strip())
    logs = get_logs(lines=args)
    await msg.answer(logs)
