from  aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from Keyboards.create_kb import place_kb, date_kb, time_kb
from state.create import CreateState


async def create_game(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберете место для игры', reply_markup=place_kb())
    await state.set_state(CreateState.place)


async def select_place(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'вы выбрали место \n'
                              f'Дальше выберите дату: ', reply_markup=date_kb())

    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.date)

async def select_date(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Я сохранил дату игры \n'
                              f'Выберете время игры', reply_markup=time_kb())
    await state.update_data(data=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.time)
