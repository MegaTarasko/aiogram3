from aiogram import Bot
from aiogram.types import Message
from utils.database import Database
import os


async def view_profile(message: Message, bot: Bot):
    db = Database(os.getenv('DATABASE_NAME'))
    games = db.db_select_column('games', 'status', 0)
    if games:
        await bot.send_message(message.from_user.id, f'Артуальные игры: ')
        for game in games:
            await bot.send_message(message.from_user.id, f'Игра состоится {game[2]} в {game[3]} \n\n'
                                                         f'Минимум : {game[4]} \n\n'
                                                         f'Максимум : {game[5]} \n\n'
                                                         f'Стоимость : {game[6]} ')

    else:
        await bot.send_message(message.from_user.id, f'Игр нет')