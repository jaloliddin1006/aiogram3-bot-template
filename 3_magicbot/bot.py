import asyncio
from handlers import bot_messages, user_commands, questionaire
from callbaks import pagination
from middlewares.check_sub import CheckSubs
from middlewares.antiflood import AntifloodMiddleware
from utils.set_bot_commands import (
    set_private_default_commands, 
    set_adminstrators_defoult_commands,
    set_group_defoult_commands
)
from utils.bot_start import on_startup_notify
from loader import bot, dp


async def main():
    
    dp.message.middleware(CheckSubs())
    # dp.message.middleware(AntifloodMiddleware())
    
    dp.include_routers(
        user_commands.router,
        questionaire.router,
        pagination.router,
        bot_messages.router
    )
    await set_private_default_commands(bot)
    await on_startup_notify(bot)

    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot, skip_updates=True)
    # print("tugadi")
    
if __name__ == '__main__':
    asyncio.run(main())