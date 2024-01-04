import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(token='6529247005:AAFHWy-ut1XU_FbvbsJpHsSbYrDWNIxIqxg', parse_mode='HTML')
dp = Dispatcher()


@dp.message(F.text == 'ping')
async def ping_pong(message: Message):
    await message.answer(f'Hello <b>{message.from_user.full_name}!</b>')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    asyncio.run(main())