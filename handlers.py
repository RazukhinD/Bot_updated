import random
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
import game
from config import dp
import text
from keyboard import kb

@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name} {text.greeting}',reply_markup=kb)


@dp.message_handler(commands=['rules'])
async def write_rules(message:Message):
    await message.answer(text=f'{message.from_user.username}'
                              f' На столе лежит {game.total} конфет.'
                              f'Ты играешь против компьютера. Первый ход определяется жеребьёвкой.'
                              f' За один ход можно забрать не более чем 28 конфет.'
                              f' Все конфеты оппонента достаются сделавшему последний ход. Начинаем игру? Если да пиши /new_game')

@dp.message_handler(commands=['new_game'])
async def start_new_game(message:Message):
    game.new_game()
    if game.check_game():
        toss = random.randint(0,1)
        if toss==0:
            await player_turn(message)
        else:
            await bot_turn(message)

async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name}, твой ход. Сколько конфет ты возьмешь себе')

@dp.message_handler(commands=['set_total'])
async def set_total_candies(message:Message):
    if not game.check_game():
        max_total=message.text
        if len(max_total)>1 and max_total[0].isdigit():
            game.set_max_total(int(max_total[0]))
            await message.reply(text=f'Максимальное количество изменено на {max_total[0]}')
        else:
            await message.reply(text='Этой командой можно настроить максимальное количество конфет. Введите /set_total и целое число')
    else:
        await message.reply(text='Настройки можно менять только в конце игры')

@dp.message_handler(commands=['bot_level'])
async def set_bot_level(message:Message):
    if not game.check_game():
        game.change_level()
        await message.reply(text=f'Уровень сложность установлен {game.bot_level}')
    else:
        await message.reply(text='Настройки можно менять только в конце игры')


@dp.message_handler()
async def take(message:Message):
    name=message.from_user.first_name
    if game.check_game():
        if message.text.isdigit():
            take=int(message.text)
            if (0<take<29) and take<= game.get_total():
                game.take_candies(take)
                if await check_win(message,'player'):
                    return
                await message.answer(f'{name} взял {take} конфет. На столе осталось: {game.get_total()}. Ходит бот.')
                await bot_turn(message)
            else:
                await message.answer('Не я же объяснял правила, проверь количество конфет')
        else:
            pass

async def bot_turn(message:Message):
    total=game.get_total()
    take=0
    if game.bot_level=='light':
        if total<=28:
            take=total
        else:
            take=random.randint(1,28)
    else:
        if total <= 28:
            take = total
        else:
            var = (game.get_total() - 29) % 28
            take = var if var>0 else random.randint(1,28)
    game.take_candies(take)
    await message.answer(f' Бот взял {take} конфет и их осталось {game.get_total()}')
    if await check_win(message,'bot'):
        return
    await player_turn(message)



async def check_win(message:Message,player: str):
    if game.get_total()==0:
        await message.answer(f'Победил {message.from_user.first_name}!' if player=='player' else 'Ну ты и даешь, искуственный интелект тебя обыграл!')
        game.new_game()
        return True
    else:
        return False
