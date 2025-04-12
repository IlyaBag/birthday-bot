from create_bot import bot, scheduler
from repo.json_storage import get_person_by_birthday
from utils.date import get_today_date_str
from utils.messages import send_msg
from utils.users import get_all_users_ids


# time of the day in tuple[hour, minute, second] for birthday notifications
NOTIFICATION_TIME = (7, 56, 0)
# permissible delay in seconds to scheduled task executing
MISSFIRE_GRACE_TIME_SEC = 60 * 30


async def send_birthday_notification() -> None:
    """Check if anyone has a birthday today and, if so, send a notification to
    all users."""

    today = get_today_date_str()
    person = get_person_by_birthday(today)
    if person is not None:
        users = get_all_users_ids()
        await send_msg(bot=bot,
                 msg=f'🎂Сегодня день рождения отмечает:\n{person}',
                 users_id=users)

def add_sched_tasks() -> None:
    hour, minute, second = NOTIFICATION_TIME
    scheduler.add_job(send_birthday_notification,
                      trigger='cron',
                      misfire_grace_time=MISSFIRE_GRACE_TIME_SEC,
                      hour=hour, minute=minute, second=second)
