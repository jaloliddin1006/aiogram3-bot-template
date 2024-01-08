import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message, CallbackQuery
import _2_keyboards as kb
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

bot = Bot(token='6943714998:AAE5bM3yB-rhRjia38UjRsXDOfQU24YKT_c', parse_mode='HTML')
dp = Dispatcher()

smiliki = [
    ["🥑", "menga avakado yoqadi"],
    ["🍎", "menga olma yoqadi"],
    ["🍐", "menga olcha yoqadi"],
    ["🍊", "menga apelsin yoqadi"],
    ["☁️", "ob havo ancha yaxshi"]
    
]


@dp.callback_query(kb.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: kb.Pagination):
    current_page = int(callback_data.page)
    action = callback_data.action
    page = current_page - 1 if current_page>0 else 0
    if action == 'next':
        page = current_page + 1 if current_page<len(smiliki)-1 else current_page
    
    with suppress(TelegramBadRequest):
        await call.message.edit_text(text=f"{smiliki[page][0]} {smiliki[page][1]}", reply_markup = kb.paginator(page))
    await call.answer()
    # await call.answer("xatolik!!", show_alert=True)


@dp.message(CommandStart())
async def ping_pong(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}!</b> start bosildi', reply_markup=kb.main_kb)


# @dp.message(F.text.lower().startswith('ssilki'))
@dp.message(F.text.lower() == 'ssilki')
async def smailiki(message: Message):
    await message.answer(f'ssilki tanlandi', reply_markup=kb.ssilki_kb)


@dp.message(F.text.lower() == 'maxsus btn')
async def maxsus_func(message: Message):
    await message.answer(f'maxsus btn tanlandi', reply_markup=kb.maxsus_btn)


@dp.message(F.text.lower() == 'calculator')
async def calc(message: Message):
    await message.answer(f'calculator tanlandi', reply_markup=kb.calc_kb())


@dp.message(F.text.lower() == 'smayliki')
async def smailiki(message: Message):
    await message.answer(f"{smiliki[0][0]} {smiliki[0][1]}", reply_markup=kb.paginator())


@dp.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)
    
    
async def main():
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    asyncio.run(main())