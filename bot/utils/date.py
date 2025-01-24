from datetime import date


def get_today_date_str() -> str:
    """Return string with today date in format DD.MM"""
    today = date.today()
    return f'{today:%d.%m}'
