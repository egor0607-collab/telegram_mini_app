"""
Telegram-бот с кнопкой запуска Mini App "Кофейная Карта России".
Требуется: pip install aiogram==3.4.1 python-dotenv fastapi uvicorn
"""
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8864861823:AAEkIbiI1mdUZLnZ2dx13gDC9NB56s_aM1k")       # токен от @BotFather
WEBAPP_URL = os.getenv("https://github.com/egor0607-collab/telegram_mini_app")          # https-ссылка на ваш захостенный index.html

bot = Bot(token=8864861823:AAEkIbiI1mdUZLnZ2dx13gDC9NB56s_aM1k)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="☕ Открыть Кофейную Карту России",
            web_app=WebAppInfo(url=https://github.com/egor0607-collab/telegram_mini_app)
        )]
    ])
    await message.answer(
        "Добро пожаловать в «Кофейную Карту России»! 🇷🇺\n"
        "Собирай регионы, отмечай маршруты и открывай ачивки за каждый купленный дрип.",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
