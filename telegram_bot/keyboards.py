from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_tee_menu = KeyboardButton("/tee_menu")

start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_kb.add(button_tee_menu)


button_coffee_menu = KeyboardButton("/coffee_menu")

coffee_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
coffee_kb.add(button_coffee_menu)
