from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def add_to_cart_btn(product_id: int, count: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➖", callback_data=f"minus_count"),
            InlineKeyboardButton(text=str(count), callback_data=f"count_{product_id}"),
            InlineKeyboardButton(text="➕", callback_data=f"plus_count"),
        ],
        [
            InlineKeyboardButton(text="🛒 Savatga qo'shish", callback_data=f"add_to_cart:{product_id}")
        ]
    ])


def get_order(user_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Buyurtma berish", callback_data=f"order:{user_id}")
        ]
    ])