from aiogram import *
import logging
from secret_token import TOKEN
from commands_list import order_tee, price_tee, coffe_order, coffe_price

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)
# first Need rename foo
# add button
# try upload info about target with Exel

@dp.message_handler(commands=(order_tee[0]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[0]} tee: price {price_tee[0]}")


@dp.message_handler(commands=(order_tee[1]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[1]} tee: price {price_tee[1]}")


@dp.message_handler(commands=(order_tee[2]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[2]} tee: price {price_tee[2]}")


@dp.message_handler(commands=(order_tee[3]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[3]} tee: price {price_tee[3]}")


@dp.message_handler(commands=(order_tee[4]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[4]} tee: price {price_tee[4]}")


@dp.message_handler(commands=(order_tee[5]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[5]} tee: price {price_tee[5]}")


@dp.message_handler(commands=(order_tee[6]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[6]} tee: price {price_tee[6]}")


@dp.message_handler(commands=(order_tee[7]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[7]} tee: price {price_tee[7]}")


@dp.message_handler(commands=(order_tee[8]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[8]} tee: price {price_tee[8]}")


@dp.message_handler(commands=(order_tee[9]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[9]} tee: price {price_tee[9]}")


@dp.message_handler(commands=(coffe_order[0]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[0]} : price {coffe_price[0]}")


@dp.message_handler(commands=(coffe_order[1]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[1]} : price {coffe_price[1]}")


@dp.message_handler(commands=(coffe_order[2]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[2]} : price {coffe_price[2]}")


@dp.message_handler(commands=(coffe_order[3]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[3]} : price {coffe_price[3]}")


@dp.message_handler(commands=(coffe_order[4]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[4]} : price {coffe_price[4]}")


@dp.message_handler(commands=(coffe_order[5]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[5]} : price {coffe_price[5]}")


@dp.message_handler(commands=(coffe_order[6]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[6]} : price {coffe_price[6]}")


@dp.message_handler(commands=(coffe_order[7]))
async def call_coffe(message: types.Message):
    await message.answer(f"You are target {coffe_order[7]} : price {coffe_price[7]}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
