import asyncio
from aiogram import Bot, Dispatcher
from handlers import bot_messages, user_commands, questionaire
from callbaks import pagination
from config_reader import BOT_TOKEN
from middlewares.check_sub import CheckSubs
from middlewares.antiflood import AntifloodMiddleware


async def main():
    
    bot = Bot(BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    
    dp.message.middleware(CheckSubs())
    dp.message.middleware(AntifloodMiddleware(2))
    
    dp.include_routers(
        user_commands.router,
        questionaire.router,
        pagination.router,
        bot_messages.router
    )

    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)
    
if __name__ == '__main__':
    asyncio.run(main())