from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from keyboards.inline import sub_channel
from cachetools import TTLCache # pip install cachetools

class AntifloodMiddleware(BaseMiddleware):
    def __init__(self, time_limit: int=2) -> None:
        self.limit = TTLCache(maxsize=1000, ttl=time_limit)
        
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
        event: Message, 
        data: Dict[str, Any]
        ) -> Any:
        
        if event.chat.id in self.limit:
            # return await event.answer("Sizni flood qilish uchun bloklayman")
            return
        else:
            self.limit[event.chat.id] = None