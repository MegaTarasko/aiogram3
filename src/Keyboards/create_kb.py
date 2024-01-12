from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.database import Database
import os 

def place_kb():
    db = Database(os.getenv('DATABASE_NAME'))
    print(db)