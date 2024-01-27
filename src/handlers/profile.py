from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from Keyboards.profile_kb import date_kb, add_match, delete_match
from utils.database import Database
import os
from utils.function import list_gamer


async def view_game(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберете дату игры', reply_markup=date_kb())

async def view_game_date(call: CallbackQuery):
    await call.answer()
    data = call.data.split("_")[-1]
    db = Database(os.getenv('DATABASE_NAME'))
    games = db.select_games('0', data)
    if (games):
        await call.message.answer(f'Актуальные игры:')
        for game in games:
            players = db.select_player(game[0])
            gamers = list_gamer(players)
            msg = (f'Игра состоится: {game[9]} Адрес: {game[10]} \n\n'
                   f'{game[2]} в {game[3]} \n\n'
                   f'Количество участников от {game[4]} до {game[5]} \n\n'
                   f'Стоимость игры {game[6]} \n\n'
                   f'{gamers}')

            if not(db.check_user(game[0], call.from_user.id)):
                await call.message.answer(msg, reply_markup=add_match(game[0], call.from_user.id))
            else:
                await call.message.answer(msg, reply_markup=delete_match(game[0], call.from_user.id))
    else:
        await call.message.answer(f'игр в этот день нет')

async def add_match_plaeyr(call: CallbackQuery):
    db = Database(os.getenv('DATABASE_NAME'))
    game = db.select_game(0, call.data.split('_')[-2])
    if not (db.check_user(game[0], call.from_user.id)):
        db.add_user_match(game[0], call.from_user.id)
        players = db.select_player(game[0])
        gamers = list_gamer(players)
        msg = (f'Игра состоится: {game[9]} Адрес: {game[10]} \n\n'
               f'{game[2]} в {game[3]} \n\n'
               f'Количество участников от {game[4]} до {game[5]} \n\n'
               f'Стоимость игры {game[6]} \n\n'
               f'{gamers}')

        await call.message.edit_text(msg, reply_markup=delete_match(game[0], call.from_user.id))

async def delete_match_plaeyr(call: CallbackQuery):
    db = Database(os.getenv('DATABASE_NAME'))
    game = db.select_game(0, call.data.split('_')[-2])
    if not (db.check_user(game[0], call.from_user.id)):
        db.add_user_match(game[0], call.from_user.id)
        players = db.select_player(game[0])
        gamers = list_gamer(players)
        msg = (f'Игра состоится: {game[9]} Адрес: {game[10]} \n\n'
               f'{game[2]} в {game[3]} \n\n'
               f'Количество участников от {game[4]} до {game[5]} \n\n'
               f'Стоимость игры {game[6]} \n\n'
               f'{gamers}')

        await call.message.edit_text(msg, reply_markup=add_match(game[0], call.from_user.id))