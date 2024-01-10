from data.config_reader import BOT_TOKEN
from aiogram import Bot, Dispatcher

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()