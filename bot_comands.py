from bot_config import dp,bot
from aiogram import types
from random import randint as rnd
from string import *

global total
global whos_turn
whos_turn=0
global turn
@dp.message_handler(commands=['start'])
async def start_bot(message:types.message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', привет! \n Всё, что я могу - предложить тебе сыграть в игру с конфетами \n жми /game, если интересно!')          

@dp.message_handler(commands=['game'])
async def start_bot(message:types.message):
    global total
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name}'
                                                      f', На столе 150 конфет, мы берём поочереди от 1 до 28 конфет. Тот, кто заберёт последнюю конфету - победил. \n пиши "Беру - Х", где Х - количество конфет, которое ты берёшь в этому ходу. Удачи! \n Право первого хода разыграем жребием.')          
    total=150
    whos_turn=rnd(1,2)
    if whos_turn==1:#bot
        turn=total%29
        if turn==0:
            turn=rnd(1,29)
        await bot.send_message(message.from_user.id, text=(f'Жребий выпал мне! Я взял {turn} конфет, а в куче остлось {total -turn} штук. \n Твой ход, не забудь: "Беру Х"'))         
        total-=turn
    else: #player
        await bot.send_message(message.from_user.id, text=(f'Жребий выпал тебе! Бери конфеты первым. \n Не забудь: "Беру Х"'))

@dp.message_handler()
async def take_player(message: types.Message):
    global total
    if "беру" in message.text.lower():
        try: take_p = int(message.text.split()[1])
        except: 
            await bot.send_message(message.from_user.id, text=('Извини, распознаю только "Беру - Х" и команды "/start" и "/game""'))
            return
        print(take_p)
        print(f'он хочет взять {take_p} конфет')
        if total<0:
            if whos_turn == 1:
                await bot.send_message(message.from_user.id, text=('А выиграл уже, оказывается, бот! Можешь начать игру заново, просто введи /game снова'))
            if whos_turn == 2:
                await bot.send_message(message.from_user.id, text=('А ведь ты уже выиграл! Можешь начать игру заново, просто введи /game снова'))
                total=0
                whos_turn=0
        elif 0<take_p<29:
            total-=take_p
            await bot.send_message(message.from_user.id, text=(f'Ты взял {take_p} Конфет.\n Осталось {max(0,total)} конфет на столе'))
            turn=total%29
            if turn==0:
                turn=rnd(1,29)
            if total<=0:
                await bot.send_message(message.from_user.id, text=('Ты выиграл, поздравляю!'))
                total=0
                whos_turn=0
                return
            total-=turn
            await bot.send_message(message.from_user.id, text=(f'Сходился бот, забрал {turn} конфет, в куче осталось {total} штук'))
            if total<=0:
                await bot.send_message(message.from_user.id, text=('Бот выиграл...\n Можешь начать игру заново, просто введи /game снова!'))
                total=0
                whos_turn=0
                return
        else:
            await bot.send_message(message.from_user.id, text=('Кажется, ты пытался мухлевать. \n Пробуй ходить ещё раз'))