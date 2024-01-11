from aiogram import types
from aiogram.methods import SetMyCommands

async def set_private_default_commands(bot):
    commands = [
        types.BotCommand(command="start", description="Botni qayta ishga tushirish"),
        types.BotCommand(command="help", description="Yordam olish"),
    ]

    await bot(SetMyCommands(commands=commands, scope=types.BotCommandScopeAllPrivateChats()))


async def set_group_defoult_commands(bot):
    commands = [
        types.BotCommand(command="start", description="Botni guruhda qayta ishga tushirish"),
        types.BotCommand(command="help", description="Guruhdan Yordam olish"),
    ]
    await bot(SetMyCommands(commands=commands, scope=types.BotCommandScopeAllGroupChats()))
    
    
    
async def set_adminstrators_defoult_commands(bot):
    commands = [
        types.BotCommand(command="count", description="Guruh adminstratori uchun"),
        types.BotCommand(command="info", description="Guruh adminstratori Yordam olish"),
    ]

    await bot(SetMyCommands(commands=commands, scope=types.BotCommandScopeAllChatAdministrators()))