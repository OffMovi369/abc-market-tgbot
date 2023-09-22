from .page import Page
from aiogram.types import Message

main_page = Page("main", "Здравствуйте, вас приветствует бот АBC market!\nЧего желаете?")

@main_page.button("✅ Оформить заказ")
async def create_order(message:Message):
    await message.reply("Отлично! Свяжитесь с нашим менеджером!!!!!!!!!!!!!!")

@main_page.button("❓ Популярные вопросы")
async def create_order(message:Message):
    await main_page.change(message, 'faq')

@main_page.button("🔢 Рассчитать стоимость заказа")
async def create_order(message:Message):
    await message.reply("Выберите откуда нужно осуществить доставку:")

@main_page.button("💵 Актуальный курс валют")
async def create_order(message:Message):
    ... #some goddamns........................................................................
    #.........................................................................................
