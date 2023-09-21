from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from callbacks import callbacks

main_kb = [
    [KeyboardButton(text="✅ Оформить заказ",)],
    [KeyboardButton(text="❓ Популярные вопросы")],
    [KeyboardButton(text="🔢 Рассчитать стоимость заказа")],
    [KeyboardButton(text="💵 Актуальный курс валют")],
]

main_markup = ReplyKeyboardMarkup(keyboard=main_kb, resize_keyboard=True)
