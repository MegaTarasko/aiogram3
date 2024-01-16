from aiogram.fsm.state import State, StatesGroup

class CreateState(StatesGroup):
    place = State()
    date = State()
    time = State()
    minplayer = State()
    maxplayer = State()
    price = State()
    