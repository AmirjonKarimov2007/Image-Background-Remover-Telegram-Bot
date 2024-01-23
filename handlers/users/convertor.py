from aiogram import types
from loader import dp
from utils.misc.lotin_to_krill import to_latin, to_cyrillic

@dp.message_handler()
async def translit(msg: types.Message):
    translate = msg.text
    javob = lambda text: to_cyrillic(text) if text.isascii() else to_latin(text)
    translated_text = javob(translate)
    await msg.reply(translated_text)
