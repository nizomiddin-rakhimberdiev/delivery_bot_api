from aiogram.fsm.state import State, StatesGroup

class AddCartState(StatesGroup):
    category = State()
    product = State()
    add_cart = State()

class AddClientState(StatesGroup):
    phone = State()

class OrderState(StatesGroup):
    address = State()
    confirm = State()