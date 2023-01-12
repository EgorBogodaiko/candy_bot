from bot_config import dp,bot
from aiogram import types
import constants
list=constants.ABILITIES
from search_rows import search
from show_bd import show_all_bd
from checkers import *
global value
global field                        
db_name = constants.DATA_BASE_NAME

@dp.message_handler(commands=['start'])
async def start_bot(message:types.message):
    global value
    value=""
    global field
    field=""
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', привет! \n Всё, что я могу - предложить тебе поработать с БД. \n Список действий:\n'
                                                      f'{list}')

@dp.message_handler(commands=['Show'])
async def show_bd(message:types.message):
    await show_all_bd(message,db_name)

@dp.message_handler(commands=['Search'])
async def search_bd(message:types.message):
    if field=="" or value=="":
        await bot.send_message(message.from_user.id, text='Для поиска нам понадобится поле, по которому будем и скать и значение, которое нужно будет искать в строках по этому полю. \nЧтобы указать поле, пиши\n/field "Имя поля после пробела"\nЧтобы указать значение для поиска: /Value "Значение поля после пробела"\nЗатем просто снова введи /Search')
    else:
        await search(message,db_name,field,value,1)

@dp.message_handler(commands=['Field'])
async def field_fill(message:types.message):
    global field
    try:
        presplut=message.text.split(' ')[1]
    except:
        await bot.send_message(message.from_user.id, text='Через пробел введи имя поля')
        return
    if checker_field(str(message.text.split(' ')[1]))==True:
        field = str(message.text.split(' ')[1])
        print(field)
    else:
        await bot.send_message(message.from_user.id, text='Нет такого поля')
        
@dp.message_handler(commands=['Value'])
async def value_fill(message:types.message):
    global field
    global value
    if field!="":
        try:
            presplut=message.text.split(' ')[1]
        except:
            await bot.send_message(message.from_user.id, text='Через пробел введи значение')
            return
        if checker_field_val(field,(str(message.text.split(' ')[1])))==True:
            value = message.text.split(' ')[1]
            print(value)
        else:
            await bot.send_message(message.from_user.id, text='Значение не соответствует формату поля')
    else:
        await bot.send_message(message.from_user.id, text="Не введено поле")