from aiogram import Bot
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup


callbacks = {}
keyboards = {}
markups= {}

def add_to_keyboard(group:str, button_text:str, row:int):
    global markups
    if not(keyboards.get(group)):
        keyboards[group] = []
        markups[group] = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True)
    
    keyboard = keyboards[group]
    if row:
        keyboard[row].append(KeyboardButton(text=button_text))
    else:
        keyboard.append([KeyboardButton(text=button_text)])

    markups[group].keyboard = keyboard
    



# callback to button register
def register_cb(group:str, button_text:str, row:int=None):
    def decorator(function):
        global callbacks
        async def wrapper(bot:Bot, message:Message):
            result = await function(bot, message)
            return result
        callbacks.update({button_text: wrapper})
        add_to_keyboard(group, button_text, row)
        return wrapper
    return decorator

async def execute_command(bot: Bot, message:Message) -> bool:
    command = message.text
    cb = callbacks.get(command)
    if cb:
        await cb(bot, message)
        return True
    else:
        return False