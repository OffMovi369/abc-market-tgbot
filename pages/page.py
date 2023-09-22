from aiogram import Bot
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from user import User, UserHandle

class Page:
    __pages = {}
    bot:Bot

    def __init__(self, name:str, index_text:str):
        self.name = name
        self.keyboard = []
        self.callbacks = {}
        self.data_handlers = {}
        self.index_text=index_text
        Page.__pages.update({name:self})
    
    def button(self, text:str, row:int=None):
        def decorator(function):
            async def wrapper(message:Message):
                result = await function(message)
                return result
            self.callbacks.update({text: wrapper})
            # Create a keyboard for every button
            if row is None:
                self.keyboard.append([KeyboardButton(text=text)])
            else:
                self.keyboard[row].append(KeyboardButton(text=text))
            return wrapper
        return decorator


    async def change(self,message:Message, new_page_name:str, text:str=None):
        user = UserHandle.get_user(message.from_user.id)
        user.previous_page = self.name
        new_page = Page.get_page(new_page_name)
        
        await message.answer(text if text else new_page.index_text, reply_markup=new_page.markup)
        user.current_page = new_page_name


    def create_markup(self):
        self.markup = ReplyKeyboardMarkup(keyboard= self.keyboard, resize_keyboard=True)
            
    @classmethod
    def get_page(cls, name:str):
        return cls.__pages.get(name)