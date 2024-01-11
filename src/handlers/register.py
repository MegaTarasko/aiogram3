from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from state.register import RegisterState
import re
import os
from utils.database import Database


async def start_register(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(message.from_user.id, f'Вы уже зарегистрированы под именем {users[1]}')
    else:
        await (message.answer(f'Начнем регистрацию \n Как вас зовут?'))
        await state.set_state(RegisterState.regName)

async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'привет, пользователь {message.text} \n'
                        f'укажите номер телефона 📱')
    await state.update_data(regname= message.text)
    await state.set_state(RegisterState.regPhone)

async def register_phone(message: Message, state: FSMContext, bot: Bot):
    if(re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        reg_date = await state.get_data()
        reg_name = reg_date.get('regname')
        reg_phone = reg_date.get('regphone')

        msg = f'Регистрация успешна, {reg_name} \n\n Телефон - {reg_phone}'
        await bot.send_message(message.from_user.id, msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()

    else:
        await bot.send_message(message.from_user.id, f'телефон неверен ❌')
    