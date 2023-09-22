import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from config import BOT_TOKEN, ADMINS_ID
from user import UserHandle, Status
from pages.page import Page

bot = Bot(token=BOT_TOKEN)          
dp = Dispatcher()
Page.bot = bot

@dp.message(F.text == "/start")
async def start(message: Message):
    main_page = Page.get_page("main")
    await message.answer(main_page.index_text, reply_markup=main_page.markup) 

@dp.message(F.text == "/id")
async def user_id(message: Message):
    await message.answer(f"Ваш id: {message.from_user.id}")

@dp.message((F.text == "/set") & (F.from_user.id.in_(ADMINS_ID)))
async def set_currency(message:Message):
    args = message.text.split()
    await message.answer(str(args))

@dp.message()
async def message_listener(message: Message):
    user = UserHandle.get_user(message.from_user.id)
    text = message.text
    current_page = Page.get_page(user.current_page)
    match user.status:
        case Status.command:
            handle_function = current_page.callbacks.get(text)
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