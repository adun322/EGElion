import json

from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, Bot
from jsonf import write_inf

TOKEN = '8163542920:AAGRn2L3EvzPKijEKQKsaXQeONWyeNQC1No'
bot = Bot(TOKEN)
router = Router()


@router.message(CommandStart())
async def start(message: Message):
    user_id = str(message.from_user.id)
    data = {user_id: {}}
    for i in range(13):
        data[user_id][i] = "0"
    write_inf(data, "db_users.json")
    await message.reply('Привет! Я Ева, учусь В ЕГЭлеоне, как и ты. Я буду следить за тобой и напоминать тебе тренироваться!')


# отправка стикеров (ачивок)
async def sticker1(user_id, ind):
    if ind == 1:
        await bot.send_sticker(user_id, sticker="CAACAgIAAxkBAAEJIflnCp3HIXITOHCCvu_9WTkte7qlxwACil4AAnF0UEj4ba56-wlu-DYE")
    elif ind == 2:
        await bot.send_sticker(user_id, sticker="CAACAgIAAxkBAAEJIftnCp3KbGN61kxoJCbWhLPpjQ6x7wACc10AAnUbUEiisgABlE1abxY2BA")
    elif ind == 3:
        await bot.send_sticker(user_id, sticker="CAACAgIAAxkBAAEJIf1nCp3LW1lNqZzqjc0FnhE-6sdaywACclIAAlsCUUgP78XRAAHWiAk2BA")
    else:
        await bot.send_sticker(user_id, sticker="CAACAgIAAxkBAAEJIf9nCp3Ol36wSfcbjFAH4EMkNd8JTAACul4AAmitWUhJxAuAZ0486DYE")


# @router.message()
# async def text(message: Message):
#     user_id = message.from_user.id
