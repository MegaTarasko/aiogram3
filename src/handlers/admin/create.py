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
    await state.update_data(date=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.time)


async def select_time(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Укажите минимальное количество игроков от 4 до 16')
    await state.update_data(time=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.minplayer)

async def select_minplayer(message: Message, state: FSMContext, bot: Bot):
    if(message.text.isdigit() and 4 <= int(message.text) <= 16):
        await bot.send_message(message.from_user.id, f'Теперь укажите максимальное количество игроков от 4 до 16')
        await state.update_data(minplayer=message.text)
        await state.set_state(CreateState.maxplayer)
    else:
        await bot.send_message(message.from_user.id, f'Ошибка в веденных данных')

async def select_maxplayer(message: Message, state: FSMContext, bot: Bot):
    if(message.text.isdigit() and 4 <= int(message.text) <= 16):
        await bot.send_message(message.from_user.id, f'Укажите стоимость игры')
        await state.update_data(maxplayer=message.text)
        await state.set_state(CreateState.price)
    else:
        await bot.send_message(message.from_user.id, f'Ошибка в веденных данных')

async def select_price(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Отлично, я записал')
    await state.update_data(price=message.text)
    create_data = await state.get_data()
    print(create_data)