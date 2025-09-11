from aiogram.fsm.state import State, StatesGroup

class AddCartState(StatesGroup):
    category = State()
    product = State()
    add_cart = State()