import json
import os

from decouple import config  # type: ignore

from exceptions.exc import StoragePathError


NO_BIRTHDAY_PERSON_MSG = 'В этот день у нас нет именинников'


def get_all_birthdays() -> dict[str, str]:
    storage_path = config('STORAGE_PATH', default='birthdays.json')
    if not os.path.exists(storage_path):
        raise StoragePathError(f'Storage path "{storage_path}" does not exist.')
    with open(storage_path, 'r') as f:
        birthdays = json.load(f)
    return birthdays

def get_person_by_birthday(date: str) -> str:
    all_birthdays = get_all_birthdays()
    birthday = all_birthdays.get(date, NO_BIRTHDAY_PERSON_MSG)
    return birthday
