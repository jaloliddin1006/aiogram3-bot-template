from aiogram import Router, F
import random
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from keyboards import reply


router = Router()

@router.message(CommandStart())
async def ping_pong(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}!</b> start bosildi', reply_markup=reply.main)


@router.message(Command(commands=['rn', 'random']))
async def ping_pong(message: Message, command: CommandObject):
    a, b = list(map(int, command.args.split("-")))    
    rnum = random.randint(a, b)
    await message.answer(f'Random number: {rnum}')


@router.message(F.text.lower() == 'orqaga')
async def back(message: Message):
    await message.answer(f'Asosiy sahifa', reply_markup=reply.main)