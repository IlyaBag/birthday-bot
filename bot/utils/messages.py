from typing import Sequence

from aiogram import Bot


async def send_msg(bot: Bot, msg: str, user_id: int | Sequence[int]) -> None:
    """Send a message from the bot to one or several users."""
    if isinstance(user_id, int):
        await bot.send_message(chat_id=user_id, text=msg)
    else:
        for uid in user_id:
            await bot.send_message(chat_id=uid, text=msg)
