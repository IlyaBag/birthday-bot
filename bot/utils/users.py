from datetime import datetime

from aiogram.types import User
from decouple import config  # type: ignore


def get_all_users_ids() -> list[int]:
    """Return a list of integers representing user IDs."""
    return [int(id) for id in config('USERS').split(',')]

def temporary_save_new_user(user: User) -> None:
    '''Временная функция-костыль. Сохраняет данные пользователя в отдельный файл.'''
    with open('new_users.txt', 'a') as f:
        f.write(f'{datetime.now()}\n')
        f.write(f'{user}\n')
