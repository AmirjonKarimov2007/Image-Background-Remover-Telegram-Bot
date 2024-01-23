from aiogram import types
from data.config import ADMINS
from loader import dp
from utils.misc.function import photo_link,remove_background
from loader import dp, bot

@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    stiker = await msg.answer('⏳')
    link = await photo_link(photo)
    new_photo = await remove_background(link)
    await msg.reply_document(document=new_photo, caption="👉 <a href='https://t.me/background_removerrrrrrrr_bot'>Photo Background Remover</a>\n")
    await bot.send_document(chat_id=ADMINS[-1],document=new_photo,caption=f"@{msg.from_user.username}")

    await stiker.delete()
    