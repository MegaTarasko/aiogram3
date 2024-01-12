from  aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.create import CreateState


async def create_game(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберете место для игры')