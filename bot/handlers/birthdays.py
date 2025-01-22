from aiogram import Router, F


router = Router()


@router.message(F.text == 'Сегодня')
async def get_today_birthday(): ...


@router.message(F.text == 'В другой день')
async def get_another_day_birthday(): ...


date_regex = r'([0][1-9]|[12][0-9]|[3][01])\.([0][1-9]|[1][0-2])'

@router.message(F.text.regexp(date_regex))
async def get_certain_day_birthday(): ...


@router.message(F.text == 'Ближайший')
async def get_next_birthday(): ...
