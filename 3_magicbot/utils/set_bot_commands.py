from aiogram import types
from aiogram.methods import SetMyCommands

async def set_default_commands(bot):
    commands = [
        types.BotCommand(command="start", description="Botni ishga tushirish"),
        types.BotCommand(command="help", description="Yordam olish"),
    ]

    await bot(SetMyCommands(commands=commands, scope=types.BotCommandScopeAllPrivateChats()))
