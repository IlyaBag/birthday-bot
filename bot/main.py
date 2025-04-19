import asyncio
import logging

from decouple import config

from create_bot import bot, dp as dispatcher, scheduler
from handlers.bash_exec import router as bash_router
from handlers.birthdays import router as birthday_router
from handlers.birthday_search import router as surname_router
from handlers.start import router as start_router
from utils.scheduled_tasks import add_sched_tasks


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
    handlers=[logging.StreamHandler(),
              logging.FileHandler(filename=config('LOGFILENAME'))],
)

async def start_bot():
    add_sched_tasks()
    scheduler.start()

async def main():
    dispatcher.include_routers(bash_router, birthday_router, start_router,
                               surname_router)
    dispatcher.startup.register(start_bot)
    try:
        await dispatcher.start_polling(bot)
    finally:
        scheduler.shutdown()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
