from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from keyboards.inline import sub_channel


class CheckSubs(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
        event: Message, 
        data: Dict[str, Any]
        ) -> Any:
        
        chat_member = await event.bot.get_chat_member(
            chat_id='-1001704364861', 
            user_id=event.from_user.id
            )
        # print(event)
        
        if chat_member.status == "left":
            await event.answer("Kanalga obuna bo'ling", reply_markup=sub_channel)
        else:
            return await handler(event, data)