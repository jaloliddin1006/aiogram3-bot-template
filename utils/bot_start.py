import logging
from aiogram import Bot
from data.config_reader import ADMIN_ID

async def on_startup_notify(bot: Bot):
    print("\n============= ||| Bot ishga tushdi ||| =============\n")
    for admin in ADMIN_ID:
        try:
            await bot.send_message(admin, "Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)