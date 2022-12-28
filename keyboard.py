from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb=ReplyKeyboardMarkup(resize_keyboard=True)
btn_new_game=KeyboardButton(text='/new_game')
btn_level=KeyboardButton(text='/bot_level')
btn_rules=KeyboardButton(text='/rules')


kb.add(btn_new_game,btn_level,btn_rules)