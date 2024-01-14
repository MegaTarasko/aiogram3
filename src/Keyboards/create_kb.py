from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.database import Database
import os 

def place_kb():
    db = Database(os.getenv('DATABASE_NAME'))
    places = db.db_select_all('place')
    kb = InlineKeyboardBuilder()
    for place in places:
        kb.button(text=f'{place[1]}', callback_data=f'{place[0]}')
    kb.adjust(1)
    return kb.as_markup()