from aiogram import *
import logging
from secret_token import TOKEN
from commands_list import order_tee, price_tee, coffee_order, coffee_price

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)


# first Need rename foo
# add button
# try upload info about target with Exel

@dp.message_handler(commands=(order_tee[0]))
async def call_start1(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[0]} tee: price {price_tee[0]}")


@dp.message_handler(commands=(order_tee[1]))
async def call_start2(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[1]} tee: price {price_tee[1]}")


@dp.message_handler(commands=(order_tee[2]))
async def call_start3(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[2]} tee: price {price_tee[2]}")


@dp.message_handler(commands=(order_tee[3]))
async def call_start4(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[3]} tee: price {price_tee[3]}")


@dp.message_handler(commands=(order_tee[4]))
async def call_start5(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[4]} tee: price {price_tee[4]}")


@dp.message_handler(commands=(order_tee[5]))
async def call_start6(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[5]} tee: price {price_tee[5]}")


@dp.message_handler(commands=(order_tee[6]))
async def call_start7(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[6]} tee: price {price_tee[6]}")


@dp.message_handler(commands=(order_tee[7]))
async def call_start8(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[7]} tee: price {price_tee[7]}")


@dp.message_handler(commands=(order_tee[8]))
async def call_start9(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[8]} tee: price {price_tee[8]}")


@dp.message_handler(commands=(order_tee[9]))
async def call_start10(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[9]} tee: price {price_tee[9]}")


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
