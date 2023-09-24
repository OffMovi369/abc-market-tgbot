from .page import Page
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import get_curency

main_page = Page("main", "Здравствуйте, вас приветствует бот АBC market!\nЧего желаете?")

@main_page.button("✅ Оформить заказ")
async def create_order(message:Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Связаться", url="https://t.me/UmibozUwU")]])
    await message.reply("Для оформления заказа звяжитесь с нашим менеджером!", reply_markup=markup)

@main_page.button("❓ Популярные вопросы")
async def faq(message:Message):
    await main_page.change(message, 'faq')

@main_page.button("🔢 Рассчитать стоимость заказа")
async def calc(message:Message):
    await main_page.change(message, 'calc')

@main_page.button("💵 Актуальный курс валют")
async def actual_currency(message:Message):
    currency = get_curency()
    await message.reply(f"Актуальный курс валют\n1 доллар - {currency['d']} ₽\n1 юань - {currency['y']} ₽")