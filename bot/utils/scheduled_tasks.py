from decouple import config  # type: ignore

from create_bot import bot, scheduler
from utils.date import fetch_birthday_person
from utils.messages import send_msg


async def send_birthday_notification() -> None:
    """Check if anyone has a birthday today and, if so, send a notification to
    all users."""

    person = fetch_birthday_person()
    if person:
        users = config('USERS').split(',')
        await send_msg(bot=bot,
                 msg=f'🎂Сегодня день рождения отмечает:\n{person}',
                 user_id=users)

def add_sched_tasks() -> None:
    scheduler.add_job(send_birthday_notification,
                      trigger='cron', hour=9, minute=6)
