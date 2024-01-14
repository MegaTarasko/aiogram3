from aiogram.fsm.state import State, StatesGroup

class CreateState(StatesGroup):
    place = State()
    date = State()
    time = State()
    minplayrs = State()
    maxplayrs = State()
    price = State()
    