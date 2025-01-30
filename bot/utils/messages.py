from typing import Sequence

from aiogram import Bot


async def send_msg(bot: Bot, msg: str, users_id: int | Sequence[int]) -> None:
    """Send a message from the bot to one or several users."""
    if isinstance(users_id, int):
        await bot.send_message(chat_id=users_id, text=msg)
    else:
        for user_id in users_id:
            await bot.send_message(chat_id=user_id, text=msg)
