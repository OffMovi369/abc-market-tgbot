from .callback import register_cb, markups
from aiogram import Bot
from aiogram.types import Message


group = "main"


@register_cb(group, "✅ Оформить заказ")
async def checkout(bot:Bot, message:Message):
    await message.reply("Свяжитесь с менеджером...")

@register_cb(group, "❓ Популярные вопросы")
async def checkout(bot:Bot, message:Message):
    await message.reply("Выберите интересующий Вас вопрос:", reply_markup=markups['faq'])

@register_cb(group, "🔢 Рассчитать стоимость заказа")
async def checkout(bot:Bot, message:Message):
    await message.reply("Свяжитесь с менеджером...")

@register_cb(group, "💵 Актуальный курс валют")
async def checkout(bot:Bot, message:Message):
    await message.reply("Свяжитесь с менеджером...")
