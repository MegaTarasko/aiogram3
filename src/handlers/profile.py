from aiogram import Bot
from aiogram.types import Message
from Keyboards.profile_kb import date_kb
from utils.database import Database
import os


async def view_game(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберете дату игры', reply_markup=date_kb())