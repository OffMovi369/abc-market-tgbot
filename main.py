import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from config import BOT_TOKEN, logger
import callbacks
from callbacks.callback import execute_command, markups

from user import Status, get_user

bot = Bot(token=BOT_TOKEN)          
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Здравствуйте, вас приветствует бот АBC market!\nЧего желаете?", reply_markup=markups['main'])

@dp.message(F.text == "/id")
async def user_id(message: Message):
    await message.answer(f"Ваш id: {message.from_user.id}")

@dp.message()
async def command_listener(message: Message):
    user = get_user(message.from_user.id)
    if user.status == Status.command:
        executed = await execute_command(bot, message)
    # elif user.status == Status.data:
    #     data_handled = await data_handle()


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())