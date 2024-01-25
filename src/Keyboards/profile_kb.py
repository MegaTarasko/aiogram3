from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import datetime

def profile_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Актуальные игры")
    kb.button(text="Мои игры")
    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберете действие')

def date_kb():
    kb = InlineKeyboardBuilder()
    current_date = datetime.date.today()
    for i in range(7):
        current_date += datetime.timedelta(days=1)
        kb.button(text=f"{current_date.strftime('%d.%m')}", callback_data=f"viewn_date_{current_date.strftime('%d.%m.%y')}")
    kb.adjust(1)
    return kb.as_markup()

def add_match(game_id, user_id):
    kb = InlineKeyboardBuilder()
    kb.button(text=f'Запись на матч', callback_data=f'add_match_{game_id}_{user_id}')
    kb.adjust(1)
    return kb.as_markup()

def delete_match(game_id, user_id):
    kb = InlineKeyboardBuilder()
    kb.button(text=f'Удалить запись', callback_data=f'delete_match_{game_id}_{user_id}')
    kb.adjust(1)
    return kb.as_markup()