from aiogram import *
import logging
from secret_token import TOKEN
from commands_list import order_tee, price_tee, coffee_order, coffee_price, tee_menu, coffee_menu
import keyboards as kb

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)


# first Need rename foo
# add button
# try upload info about target with Exel
# order_tee = ['bancha', 'highgrown', 'genmaicha', 'gyokuro', 'darjeeling', 'java', 'dooars', 'keemun', 'kokicha',
#             'matcha']
#@dp.message_handler(commands=['tee_menu'])
#async def start_menu_tee(message: types.Message):
#    await message.answer(f" This is  {tee_menu}", reply_markup=kb.markup_full)

@dp.message_handler(commands=['menu'])
async def process_menu(message: types.Message):
    await message.answer(f"{tee_menu} or {coffee_menu}", reply_markup=kb.markup)



@dp.message_handler(commands=(order_tee[0]))
async def order_tee_1(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[0]} tee: price {price_tee[0]}")


@dp.message_handler(commands=(order_tee[1]))
async def order_tee_2(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[1]} tee: price {price_tee[1]}")


@dp.message_handler(commands=(order_tee[2]))
async def order_tee_3(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[2]} tee: price {price_tee[2]}")


@dp.message_handler(commands=(order_tee[3]))
async def order_tee_4(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[3]} tee: price {price_tee[3]}")


@dp.message_handler(commands=(order_tee[4]))
async def order_tee_5(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[4]} tee: price {price_tee[4]}")


@dp.message_handler(commands=(order_tee[5]))
async def order_tee_6(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[5]} tee: price {price_tee[5]}")


@dp.message_handler(commands=(order_tee[6]))
async def order_tee_7(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[6]} tee: price {price_tee[6]}")


@dp.message_handler(commands=(order_tee[7]))
async def order_tee_8(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[7]} tee: price {price_tee[7]}")


@dp.message_handler(commands=(order_tee[8]))
async def order_tee_8(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[8]} tee: price {price_tee[8]}")


#@dp.message_handler(commands=['coffee_menu'])
#async def start_menu_coffee(message: types.Message):
#    await message.answer(f"This is {coffee_menu}", reply_markup=kb.coffee_kb)


@dp.message_handler(commands=(coffee_order[0]))
async def call_coffe1(message: types.Message):
    await message.answer(f"You are target {coffee_order[0]} : price {coffee_price[0]}")


@dp.message_handler(commands=(coffee_order[1]))
async def call_coffe2(message: types.Message):
    await message.answer(f"You are target {coffee_order[1]} : price {coffee_price[1]}")


@dp.message_handler(commands=(coffee_order[2]))
async def call_coffe3(message: types.Message):
    await message.answer(f"You are target {coffee_order[2]} : price {coffee_price[2]}")


@dp.message_handler(commands=(coffee_order[3]))
async def call_coffe4(message: types.Message):
    await message.answer(f"You are target {coffee_order[3]} : price {coffee_price[3]}")


@dp.message_handler(commands=(coffee_order[4]))
async def call_coffe5(message: types.Message):
    await message.answer(f"You are target {coffee_order[4]} : price {coffee_price[4]}")


@dp.message_handler(commands=(coffee_order[5]))
async def call_coffe6(message: types.Message):
    await message.answer(f"You are target {coffee_order[5]} : price {coffee_price[5]}")


@dp.message_handler(commands=(coffee_order[6]))
async def call_coffe7(message: types.Message):
    await message.answer(f"You are target {coffee_order[6]} : price {coffee_price[6]}")


@dp.message_handler(commands=(coffee_order[7]))
async def call_coffe8(message: types.Message):
    await message.answer(f"You are target {coffee_order[7]} : price {coffee_price[7]}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
