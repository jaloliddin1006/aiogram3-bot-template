import asyncio
from aiogram import Bot, Dispatcher
from handlers import bot_messages, user_commands, questionaire
from callbaks import pagination
from config_reader import BOT_TOKEN



async def main():
    
    bot = Bot(BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    
    dp.include_router(user_commands.router)
    dp.include_router(questionaire.router)
    dp.include_router(pagination.router)
    dp.include_router(bot_messages.router)

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    asyncio.run(main())