import csv
from bot_config import dp,bot
from aiogram import types


async def show_all_bd(message:types.message,db_name):
    """принимает на вход адрес БД
    выводит всю БД в консоль
    ничего не возвращает
    """
    with open(db_name) as f:
        reader = csv.reader(f,delimiter='|')
        headers = next(reader)
        await bot.send_message(message.from_user.id, text=headers)
        for row in reader:
            await bot.send_message(message.from_user.id, text=row)