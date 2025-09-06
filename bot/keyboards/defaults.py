from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests

categories = requests.get("http://127.0.0.1:8000/api/categories/").json()
products = requests.get("http://127.0.0.1:8000/api/products/").json()
print(categories)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu')
        ]
    ],
    resize_keyboard=True
)

def get_categories_btn():
    buttons = [
            [KeyboardButton(text=category['name'])]
            for category in categories
        ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def get_products_btn(category):
    buttons = [
            [KeyboardButton(text=product['name'])]
            for product in products if product['category']['name'] == category
        ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)