import json
import os

from decouple import config  # type: ignore

from exceptions.exc import StoragePathError


def get_all_birthdays() -> dict[str, str]:
    """Fetch all data about birthdays from the JSON storage and returns them in
    the form of a dictionary."""

    storage_path = config('STORAGE_PATH', default='birthdays.json')
    if not os.path.exists(storage_path):
        raise StoragePathError(f'Storage path "{storage_path}" does not exist.')
    with open(storage_path, 'r') as f:
        birthdays = json.load(f)
    return birthdays

def get_person_by_birthday(date: str) -> str | None:
    '''Находит именинника по дате дня рождения. Возвращает строку с именем
    именинника или None, если день рождения в указанную дату не найден.'''

    all_birthdays = get_all_birthdays()
    birthday = all_birthdays.get(date)
    return birthday
