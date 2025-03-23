from datetime import datetime

from aiogram.types import User
from decouple import config  # type: ignore

from repo.json_storage import get_all_users


def get_all_users_ids() -> list[int]:
    """Return a list of integers representing user IDs."""
    users = get_all_users()
    return [int(user['tg_id']) for user in users]

def temporary_save_new_user(user: User) -> None:
    '''Временная функция-костыль. Сохраняет данные пользователя в отдельный файл.'''
    with open('new_users.txt', 'a') as f:
        f.write(f'{datetime.now()}\n')
        f.write(f'{user}\n')
