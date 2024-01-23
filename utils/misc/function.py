from io import BytesIO
import aiohttp
from aiogram import types
from loader import bot


async def photo_link(photo: types.photo_size.PhotoSize) -> str:
    with await photo.download(BytesIO()) as file:
        form = aiohttp.FormData()
        form.add_field(
            name='file',
            value=file,
        )
        async with bot.session.post('https://telegra.ph/upload', data=form) as response:
            img_src = await response.json()

    link = 'http://telegra.ph/' + img_src[0]["src"]
    return link

import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"
headers = {
  "content-type": "application/x-www-form-urlencoded",
  "X-RapidAPI-Key": "e2af93470amsh08465450b0656c3p178d87jsndbaae8795483",
  "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']
  
