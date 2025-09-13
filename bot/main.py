from aiogram import Bot, Dispatcher, F, types
import asyncio
from keyboards.defaults import menu, get_categories_btn, get_products_btn
from states.states import AddCartState, AddClientState
from aiogram.fsm.context import FSMContext
import requests
from keyboards.defaults import phone_btn
from keyboards.inlines import add_to_cart_btn

bot = Bot(token="6514890915:AAH36rgB6LGAhwrhGuV_npbTc_zfu_B-CWA")
dp = Dispatcher()

@dp.message(F.text == '/start')
async def start(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    users = requests.get("http://127.0.0.1:8000/api/clients/").json()
    print('Users', users)
    clients = [c['user_id'] for c in users]
    print('Clients', clients)
    if str(user_id) not in clients:
        await message.answer("Ro'yxatdan o'tish uchun telefon raqamingizni yuboring: ", reply_markup=phone_btn)
        await state.set_state(AddClientState.phone)
    else:
        await message.answer("Assalamu alaykum", reply_markup=menu)

@dp.message(AddClientState.phone)
async def nimadir(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    print(phone)
    user_id = message.from_user.id
    requests.post("http://127.0.0.1:8000/api/clients/", json={"user_id": f"{user_id}", "phone_number": f"{phone}"})
    await message.answer("Muvaffaqiyatli ro'yxatdan o'tdizgiz!")
    await state.clear()

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
        await message.answer_photo(photo=image, caption=f"{name}\n{price} so'm\n{description}", reply_markup=add_to_cart_btn(id, 1))
        # await message.answer_photo(photo=image, caption=f"{name}\n{price} so'm\n{description}")
        await state.set_state(AddCartState.product)
    return

@dp.callback_query(F.data == 'plus_count')
async def plus_count_handler(callback_query: types.CallbackQuery):
    print("Plus bosildi")
    product_id = callback_query.message.reply_markup.inline_keyboard[0][1].callback_data.split("_")[1]
    print(product_id)
    count = int(callback_query.message.reply_markup.inline_keyboard[0][1].text)
    count += 1
    await callback_query.message.edit_reply_markup(reply_markup=add_to_cart_btn(product_id, count))


@dp.callback_query(F.data == 'minus_count')
async def minus_count_handler(callback_query: types.CallbackQuery):
    print("Minus bosildi")
    product_id = callback_query.message.reply_markup.inline_keyboard[0][1].callback_data.split("_")[1]
    count = int(callback_query.message.reply_markup.inline_keyboard[0][1].text)
    if count > 1:
        count -= 1
        await callback_query.message.edit_reply_markup(reply_markup=add_to_cart_btn(product_id, count))
    else:
        await callback_query.answer("Soni 1 dan kam bo'lishi mumkin emas!")

    
@dp.callback_query(F.data.startswith('add_to_cart'))
async def add_to_cart_handler(callback_query: types.CallbackQuery):
    product_id = int(callback_query.data.split(":")[1])
    user_id = callback_query.from_user.id
    count = int(callback_query.message.reply_markup.inline_keyboard[0][1].text)
    product = requests.get(f"http://127.0.0.1:8000/api/products/{product_id}/").json()
    print(product)
    price = product['price']
    clients = requests.get(f"http://127.0.0.1:8000/api/clients/").json()
    client_id = 0
    for c in clients:
        if c['user_id'] == str(user_id):
            client_id = c['id']
    print(client_id)
    requests.post("http://127.0.0.1:8000/api/carts/", json={'user': client_id, 'product': product_id, 'quantity': count})
    await callback_query.answer("Maxsulot savatchaga qo'shildi!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())