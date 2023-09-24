from .page import Page
from aiogram.types import Message

faq_page = Page("faq", "Выберите интересующий Вас вопрос:")

@faq_page.button("Оригинал?")
async def original(message:Message):
    await message.reply("Проект занимается поставкой исключительно оригинальных товаров! Любые проверки с вашей стороны только приветствуются!")

@faq_page.button("Стоимость доставки?",0)
async def deliver_price(message:Message):
    await message.reply("Стоимость доставки берётся фактическая, ни рубля лишнего с вас не возьмём!\nСумма доставки обговаривается, когда товар приходит в промежуточный город и к нам на склад в Краснодаре.")

@faq_page.button("Сроки доставки?",)
async def delivery_terms(message:Message):
    await message.reply("Из Китая: доставка с момента приобретения товара и доставки его на склад в Китае - около 15 дней до склада в Краснодаре (без учёта обстоятельств от нас независящих!)\nИз Европы/Америки: доставка с момента приобретения товара и доставки его на склад - около 30 дней до склада в Краснодаре (без учёта обстоятельств от нас независящих!)")

@faq_page.button("Как получить свой заказ?", 1)
async def pick_up_an_order(message:Message):
    await message.reply("Забрать можно самовывозом в Краснодаре, (адрес можно уточнить у нашего менеджера) или отправим вам заказ любым удобным для вас сервисом или транспортной компанией!")

@faq_page.button( "🔙 В главное меню")
async def back(message: Message):
    await faq_page.change(message, "main")