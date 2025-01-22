import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config

from handlers.birthdays import router as birthday_router
from handlers.start import router as start_router


bot = Bot(
    token=config('TOKEN'),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(birthday_router)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
