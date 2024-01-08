from aiogram.types import Message
from typing import Any
from aiogram.filters import BaseFilter, CommandObject


class CheckForDigit(BaseFilter):
    
    async def __call__(self, message: Message, **data: Any) -> bool:
        command: CommandObject = data.get('command')
        args = command.args
        
        if args.isdigit() or (args.count('.') == 1 and args.replace('.', '').isdigit()):
            return True 
        return False
    