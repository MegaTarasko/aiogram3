from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

import asyncio
from dotenv import load_dotenv
import os

from utils.commands import set_commands
from handlers.start import get_start
from handlers.register import start_register


load_dotenv()

token = os.getenv('TOKEN')
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='hi')

dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))

#Регистрируем хендлеры регистрации
dp.message.register(start_register, F.text=='Зарегестрироваться на сайте')

async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
