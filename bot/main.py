from aiogram import Bot, Dispatcher, F, types
import asyncio
from keyboards.defaults import menu, get_categories_btn, get_products_btn
from states.states import AddCartState
from aiogram.fsm.context import FSMContext
import requests

bot = Bot(token="6514890915:AAH36rgB6LGAhwrhGuV_npbTc_zfu_B-CWA")
dp = Dispatcher()

@dp.message(F.text == '/start')
async def start(message: types.Message):
    await message.answer("Assalamu alaykum", reply_markup=menu)

@dp.message(F.text == 'Menu')
async def start(message: types.Message, state: FSMContext):
    await message.answer("Kategoriyalardan birini tanlang: ", reply_markup=get_categories_btn())
    await state.set_state(AddCartState.category)


@dp.message(AddCartState.category)
async def nimadir(message: types.Message, state: FSMContext):
    category = message.text
    await message.answer("Maxsulotlardan birini tanlang: ", reply_markup=get_products_btn(category))
    await state.set_state(AddCartState.product)

@dp.message(AddCartState.product)
async def nimadir(message: types.Message, state: FSMContext):
    product = message.text
    id = 0
    products = requests.get("http://127.0.0.1:8000/api/products/").json()
    print(products)
    for p in products:
        if p['name'] == product:
            id = p['id']
            print(id)
    data = requests.get(f"http://127.0.0.1:8000/api/products/{id}/").json()
    print(data)
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "..", data['image'].lstrip("/"))

    image = types.FSInputFile(file_path)
    name = data['name']
    price = data['price']
    description = data['description']
    status = data['status']
    # image = types.FSInputFile(f"../.{image_url}")
    # print(image)
    if status:
        await message.answer_photo(photo=image, caption=f"{name}\n{price} so'm\n{description}")
        await state.set_state(AddCartState.product)
    return

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())