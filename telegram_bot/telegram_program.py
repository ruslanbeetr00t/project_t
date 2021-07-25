from aiogram import *
import logging
from secret_token import TOKEN
from commands_list import order_tee

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=(order_tee[0]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[0]} tee")


@dp.message_handler(commands=(order_tee[1]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[1]} tee")


@dp.message_handler(commands=(order_tee[2]))
async def call_start(message: types.Message):
    await message.answer(f"Yoa are target {order_tee[2]} tee")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
