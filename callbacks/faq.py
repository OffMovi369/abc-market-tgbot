from .callback import register_cb, markups
from aiogram import Bot
from aiogram.types import Message

group = "faq"

@register_cb(group, "Оригинал?")
async def original(bot:Bot, message:Message):
    await message.reply("Проект занимается поставкой исключительно оригинальных товаров! Любые проверки с вашей стороны только приветствуются!")

@register_cb(group, "Стоимость доставки?",0)
async def price(bot:Bot, message:Message):
    await message.reply(" Стоимость доставки берётся фактическая, ни рубля лишнего с вас не возьмём!\nСумма доставки обговаривается, когда товар приходит в промежуточный город и к нам на склад в Краснодаре.")

@register_cb(group, "Сроки доставки?",)
async def date(bot:Bot, message:Message):
    await message.reply("Из Китая: доставка с момента приобретения товара и доставки его на склад в Китае - около 15 дней до склада в Краснодаре (без учёта обстоятельств от нас независящих!)\nИз Европы/Америки: доставка с момента приобретения товара и доставки его на склад - около 30 дней до склада в Краснодаре (без учёта обстоятельств от нас независящих!)")

@register_cb(group, "Как получить свой заказ?",1)
async def give(bot:Bot, message:Message):
    await message.reply("Забрать можно самовывозом в Краснодаре, (адрес можно уточнить у нашего менеджера) или отправим вам заказ любым удобным для вас сервисом или транспортной компанией!")

@register_cb(group, "🔙 В главное меню")
async def back(bot:Bot, message: Message):
    await message.reply(reply_markup=markups['main'])