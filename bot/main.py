from aiogram import Bot, Dispatcher, F, types
import asyncio
from keyboards.defaults import menu, get_categories_btn, get_products_btn

bot = Bot(token="6514890915:AAH36rgB6LGAhwrhGuV_npbTc_zfu_B-CWA")
dp = Dispatcher()

@dp.message(F.text == '/start')
async def start(message: types.Message):
    await message.answer("Assalamu alaykum", reply_markup=menu)

@dp.message(F.text == 'Menu')
async def start(message: types.Message):
    await message.answer("Kategoriyalardan birini tanlang: ", reply_markup=get_categories_btn())

@dp.message()
async def nimadir(message: types.Message):
    category = message.text
    await message.answer("Maxsulotlardan birini tanlang: ", reply_markup=get_products_btn(category))

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())