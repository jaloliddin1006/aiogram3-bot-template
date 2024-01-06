import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
import random

bot = Bot(token='6943714998:AAE5bM3yB-rhRjia38UjRsXDOfQU24YKT_c', parse_mode='HTML')
dp = Dispatcher()


@dp.message(Command("start"))
async def ping_pong(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}!</b> start bosildi')


@dp.message(Command(commands=['rn', 'random']))
async def ping_pong(message: Message, command: CommandObject):
    a, b = list(map(int, command.args.split("-")))    
    rnum = random.randint(a, b)
    await message.answer(f'Random number: {rnum}')

@dp.message(F.text == 'play')
async def ping_pong(message: Message):
    x = await message.answer_dice(emoji='🎲')
    await asyncio.sleep(2)
    await message.answer(f'You rolled <b>{x.dice.value}</b> points!')


@dp.message(F.text == 'ping')
async def ping_pong(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}!</b>')


@dp.message()
async def empty_message(message: Message):  
    await message.answer("Bunday handler mavjud emas!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    asyncio.run(main())