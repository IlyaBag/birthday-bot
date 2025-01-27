from datetime import date

from repo.json_storage import get_person_by_birthday, NO_BIRTHDAY_PERSON_MSG


def get_today_date_str() -> str:
    """Return string with today date in format DD.MM"""
    today = date.today()
    return f'{today:%d.%m}'

def fetch_birthday_person(date: str | None = None) -> str | None:
    """Fetch a birthday person from the storage. If the `date` argument is
    omitted, then today's date is taken."""
    # NEED TO REFACTOR ! ! !

    if not date:
        date = get_today_date_str()
    person = get_person_by_birthday(date)
    if person == NO_BIRTHDAY_PERSON_MSG:
        person = None
    return person
