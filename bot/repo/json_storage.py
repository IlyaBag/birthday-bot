from datetime import datetime
import json
import logging
import os
import shutil

from aiogram.types import User
from decouple import config  # type: ignore

from exceptions.exc import StoragePathError


log = logging.getLogger(__name__)


def _open_storage() -> dict:
    """Fetch all data from the JSON storage and returns them in the form of a
    dictionary."""

    storage_path = config('STORAGE_PATH', default='storage.json')
    if not os.path.exists(storage_path):
        raise StoragePathError(f'Storage path "{storage_path}" does not exist.')
    with open(storage_path, 'r') as f:
        storage = json.load(f)
    return storage

def _write_storage(storage: dict) -> None:
    """Save new data in json storage."""
    storage_path = config('STORAGE_PATH', default='storage.json')
    if not os.path.exists(storage_path):
        raise StoragePathError(f'Storage path "{storage_path}" does not exist.')

    backup_storage_path = f'{os.path.splitext(storage_path)[0]}_BACKUP_{datetime.now()}{os.path.splitext(storage_path)[1]}'
    shutil.copy(storage_path, backup_storage_path)

    with open(storage_path, 'w') as f:
        f.write(json.dumps(storage, ensure_ascii=False, indent=2))

def get_all_birthdays() -> dict[str, str]:
    """Return a dictionary with all saved birthdays."""
    storage = _open_storage()
    return storage['birthdays']

def get_person_by_birthday(date: str) -> str | None:
    '''Находит именинника по дате дня рождения. Возвращает строку с именем
    именинника или None, если день рождения в указанную дату не найден.'''

    all_birthdays = get_all_birthdays()
    birthday = all_birthdays.get(date)
    return birthday

def get_all_users() -> list[dict]:
    storage = _open_storage()
    return storage['users']

def save_new_user(user: User) -> None:
    '''Сохраняет нового пользователя в хранилище json.'''
    storage = _open_storage()
    new_user = {
        'id': storage['users_id_sequence'],
        'tg_id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'language_code': user.language_code,
        'is_admin': False,
        'is_deleted': False,
        'created_at': str(datetime.now()),
    }
    storage['users'].append(new_user)
    storage['users_id_sequence'] += 1

    _write_storage(storage)
    log.info(f'Saved new user: {new_user}')
