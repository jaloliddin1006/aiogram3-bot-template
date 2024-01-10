from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from data.config_reader import CHANNEL_ID, ADMIN_ID
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from keyboards.builders import check_channel_sub


class CheckSubs(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
        event: Message, 
        data: Dict[str, Any]
        ) -> Any:
        
        if not event.chat.type == "private":
            return await handler(event, data)
        
        final_status = True
        unsubscribe_channels = []
        for channel in CHANNEL_ID:
            # link = await event.bot.export_chat_invite_link(channel)
            # channel_name = (await event.bot.get_chat(channel)).title
                
            try:
                
                link = await event.bot.export_chat_invite_link(channel)
                channel_name = (await event.bot.get_chat(channel)).title
                
                chat_member = await event.bot.get_chat_member(
                    chat_id=channel, 
                    user_id=event.from_user.id
                    )
                
            except TelegramBadRequest:
                await event.bot.send_message(
                    ADMIN_ID[0], 
                    f"Bot <a href='tg{link}'>{channel_name}</a>  admin emas. Kanalga admin qiling!"
                    )
                continue
                
            except Exception as err:
                await event.bot.send_message(
                    ADMIN_ID[0], 
                    f"Bot {channel} kanal navbatida xatolik: {err}"
                    )
                continue
            
            if chat_member.status == "left":

                unsubscribe_channels.append((channel_name, link))
                final_status = False
        
        if not final_status:
            # print(unsubscribe_channels)
            await event.answer("Botdan to'liq foydalanish uchun quidagi kanallarga obuna bo'ling.", reply_markup=check_channel_sub(unsubscribe_channels))
        else:
            return await handler(event, data)