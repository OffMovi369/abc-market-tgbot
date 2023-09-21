from aiogram import Bot
from aiogram.types import Message

callbacks = {}


# callback to button register
def callback(button_text, row=None):
    def decorator(function):
        global callbacks
        async def wrapper(bot:Bot, message:Message):
            result = await function(bot, message)
            return result
        callbacks.update({button_text: wrapper})
        return wrapper
    return decorator

@callback("✅ Оформить заказ")
async def checkout(bot:Bot, message:Message):
    await message.reply("Свяжитесь с менеджером...")
