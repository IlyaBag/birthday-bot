from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from create_bot import bot
from keyboards import birthday_kb as kb
from keyboards.logs_kb import logs_kb
from utils.cli_commands import get_logs, get_raspberry_cpu_temp


router = Router()

@router.message(F.text == kb.BTN_TEMP)
async def check_cpu_temp(msg: Message) -> None:
    temp = get_raspberry_cpu_temp()
    await msg.answer(temp)


class LogView(StatesGroup):
    viewing = State()


@router.message(F.text.startswith(kb.BTN_LOGS))
async def fetch_logs(msg: Message, state: FSMContext) -> None:
    await state.clear()
    args = None
    if len(msg.text) > 5:
        args = int(str(msg.text[5:]).strip())
    logs = get_logs(lines=args)
    answer = await msg.answer(logs, reply_markup=logs_kb())
    await state.set_state(LogView.viewing)
    await state.update_data(msg_id=answer.message_id)

@router.callback_query(F.data.startswith('logs_'), LogView.viewing)
async def delete_logs_message(call: CallbackQuery, state: FSMContext) -> None:
    if call.data == 'logs_del':
        data = await state.get_data()
        await bot.delete_message(chat_id=call.from_user.id,
                                 message_id=int(data['msg_id']))
    else:
        await call.answer()
        await call.message.delete_reply_markup()
    await state.clear()
