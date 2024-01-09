import logging

from aiogram import Bot

from data.config import ADMINS


async def on_startup_notify(bot: Bot):
    print("\n============= ||| Bot ishga tushdi ||| =============\n")
    # for admin in ADMINS:
    #     try:
    #         await dp.bot.send_message(admin, "Bot ishga tushdi")

    #     except Exception as err:
    #         logging.exception(err)