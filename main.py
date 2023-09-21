import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from config import BOT_TOKEN, logger
from keyboards import main_markup

bot = Bot(token=BOT_TOKEN)          
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Здравствуйте, вас приветствует бот АBC market!\nЧего желаете?", reply_markup=main_markup)

@dp.message(F.text == "/id")
async def user_id(message: Message):
    await message.answer(f"Ваш id: {message.from_user.id}")

@dp.message()
async def command_listener(message: Message):
    await message.answer("salut")


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())