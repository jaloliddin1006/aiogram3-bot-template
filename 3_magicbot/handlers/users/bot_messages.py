from aiogram import Router
from aiogram.types import Message
from aiogram import F
from keyboards import reply, builders, inline, fabrics
from data.subloader import get_json
from filters import IsPrivateChat


router = Router()
router.message.filter(IsPrivateChat())


# @router.message(F.text.lower().startswith('ssilki'))
@router.message(F.text.lower() == 'ssilki')
async def smailiki(message: Message):
    await message.answer(f'ssilki tanlandi', reply_markup=inline.ssilki_kb)


@router.message(F.text.lower() == 'maxsus btn')
async def maxsus_func(message: Message):
    await message.answer(f'maxsus btn tanlandi', reply_markup=reply.maxsus_btn)


@router.message(F.text.lower() == 'calculator')
async def calc(message: Message):
    await message.answer(f'calculator tanlandi', reply_markup=builders.calc_kb())


@router.message(F.text.lower() == 'smayliki')
async def smailiki(message: Message):
    smiliki = await get_json('smiles.json')
    await message.answer(f"{smiliki[0][0]} {smiliki[0][1]}", reply_markup=fabrics.paginator())


@router.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)
