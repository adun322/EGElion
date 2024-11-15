import asyncio
import json
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import FSInputFile
from aiogram import Bot, Dispatcher
from handlers import router

TOKEN = '8163542920:AAGRn2L3EvzPKijEKQKsaXQeONWyeNQC1No'
bot = Bot(TOKEN)


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(remind, "interval", seconds=3600)
    scheduler.start()
    await dp.start_polling(bot)


# напоминание в x и y часов
async def remind():
    now = datetime.now()
    if now.hour == 10 or now.hour == 20:
        with open("db_users.json", 'r') as f:
            data = json.load(f)
            for i in data:
                await bot.send_message(i, "Напоминаю выполнить ежедневную тренировку!")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
