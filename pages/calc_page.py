from .page import Page
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from user import UserHandle, Status
from config import get_curency

calc_page = Page("calc", "Выберите откуда нужно осуществить доставку:")

inline_markup = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Хочу оформить заказ!", callback_data="make_order")]])

@calc_page.button("Китай")
async def china(message:Message):
    user = UserHandle.get_user(message.from_user.id)
    user.data_name = "calc_y"
    user.status = Status.data
    await message.answer("Введите стоимость товара в 💴юанях:", reply_markup=ReplyKeyboardRemove())

@calc_page.button("Европа/США", 0)
async def europe(message:Message):
    user = UserHandle.get_user(message.from_user.id)
    user.data_name = "calc_d"
    user.status = Status.data
    await message.answer("Введите стоимость товара в 💵долларах:", reply_markup=ReplyKeyboardRemove())

@calc_page.button("🔙 В главное меню")
async def back(message: Message):
    await calc_page.change(message, "main")

@calc_page.get_data('calc_y')
async def calc_y(message:Message):
    user = UserHandle.get_user(message.from_user.id)
    value = 0
    try:
        value = float(message.text)
    except:
        await message.reply("При вводе стоимости произошла ошибка")
    else:
        currency = get_curency()
        user.country = "Китай"
        user.summ = int(value*currency['y']*1.03*1.07*1.07)
        await message.reply(f"Приблизительная стоимость заказа по курсу {currency['y']}: {user.summ} ₽\nКомиссия составит 7% от суммы заказа!", reply_markup=inline_markup)
    finally:
        user.status = Status.command
    
    await calc_page.change(message, "main")

@calc_page.get_data('calc_d')
async def calc_d(message:Message):
    user = UserHandle.get_user(message.from_user.id)
    value = 0
    try:
        value = float(message.text)
    except:
        await message.reply("При вводе стоимости произошла ошибка")
    else:
        currency = get_curency()
        user.country = "Европа/США"
        user.summ = int(value*currency['d']*1.03*1.07*1.07)
        await message.reply(f"Приблизительная стоимость заказа по курсу {currency['d']}: {user.summ} ₽\nКомиссия составит 7% от суммы заказа!", reply_markup=inline_markup)
    finally:
        user.status = Status.command
    await calc_page.change(message, "main")