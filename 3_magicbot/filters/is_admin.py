from aiogram.types import Message
from typing import List
from aiogram.filters import BaseFilter
from data.config_reader import ADMIN_ID

class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in ADMIN_ID
    
        