from decouple import config  # type: ignore

from create_bot import bot, scheduler
from repo.json_storage import get_person_by_birthday
from utils.date import get_today_date_str
from utils.messages import send_msg


NOTIFICATION_DAYS = 'mon - sun'
NOTIFICATION_TIME = (9, 6, 0)  # time of the day in tuple[hour, minute, second]


async def send_birthday_notification() -> None:
    """Check if anyone has a birthday today and, if so, send a notification to
    all users."""

    today = get_today_date_str()
    person = get_person_by_birthday(today)
    if person is not None:
        users = config('USERS').split(',')
        await send_msg(bot=bot,
                 msg=f'🎂Сегодня день рождения отмечает:\n{person}',
                 users_id=users)

def add_sched_tasks() -> None:
    hour, minute, second = NOTIFICATION_TIME
    scheduler.add_job(send_birthday_notification,
                      trigger='cron',
                      day_of_week=NOTIFICATION_DAYS,
                      hour=hour, minute=minute, second=second)
