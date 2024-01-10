from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState


async def start_register(message: Message, state: FSMContext):
    await (message.answer(f'Начнем регистрацию \n Как вас зовут?'))