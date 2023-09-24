import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery

from config import BOT_TOKEN, ADMINS_ID, get_curency, set_currency
from user import UserHandle, Status
from pages.page import Page

bot = Bot(token=BOT_TOKEN)          
dp = Dispatcher()
Page.bot = bot


@dp.message(F.text == "/start")
async def start(message: Message):
    main_page = Page.get_page("main")
    user = UserHandle.get_user(message.from_user.id)
    user.status = Status.command
    await message.answer(main_page.index_text, reply_markup=main_page.markup) 

@dp.callback_query(F.data == "make_order")
async def cb_make_order(callback:CallbackQuery):
    user = UserHandle.get_user(callback.from_user.id)
    for admin_id in ADMINS_ID:
        await bot.send_message(admin_id, f"Новый заказ от @{callback.from_user.username}\nСумма: {user.summ} ₽\nСтрана: {user.country}")
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer("Здравствуйте, благодарим, что решили воспользоваться услугами ABC market! Наш менеджер свяжется с вами в течении 5-10 минут для уточнения условий заказа!", show_alert=True)

@dp.message(F.text == "/id")
async def user_id(message: Message):
    await message.answer(f"Ваш id: {message.from_user.id}")

@dp.message((F.text.startswith("/set")) & (F.from_user.id.in_(ADMINS_ID)))
async def set_curency_command(message:Message):
    args = message.text.split()[1:]
    currency = get_curency()
    match args:
        case "d" | "D", value:
            currency.update({"d": float(value)})
            set_currency(currency)
            await message.reply(f"Курс успешно изменён! 1 доллар = {value}")
        case "y" | "Y", value:
            currency.update({"y": float(value)})
            set_currency(currency)
            await message.reply(f"Курс успешно изменён! 1 юань = {value}")
        case _:
            await message.reply("Для изменения курса необходимо написать валюту и значение.\nПример использования: /set d 99.44 (d - доллар, y - юань)")

@dp.message()
async def message_listener(message: Message):
    user = UserHandle.get_user(message.from_user.id)
    text = message.text
    current_page = Page.get_page(user.current_page)
    match user.status:
        case Status.command:
            handle_function = current_page.callbacks.get(text)
        case Status.data:
            handle_function = current_page.data_handlers.get(user.data_name)
    if handle_function:
        await handle_function(message)

    # if user.status == Status.command:
    #     executed = await execute_command(bot, message)
    # # elif user.status == Status.data:
    #     data_handled = await data_handle()


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())