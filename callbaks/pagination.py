from contextlib import suppress
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from keyboards import fabrics
from aiogram import Router, F
from data.subloader import get_json

router = Router()   

@router.callback_query(fabrics.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: fabrics.Pagination):
    smiliki = await get_json('smiles.json')
    current_page = int(callback_data.page)
    action = callback_data.action
    page = current_page - 1 if current_page>0 else 0
    if action == 'next':
        page = current_page + 1 if current_page<len(smiliki)-1 else current_page
    
    with suppress(TelegramBadRequest):
        await call.message.edit_text(text=f"{smiliki[page][0]} {smiliki[page][1]}", reply_markup = fabrics.paginator(page))
    await call.answer()
    # await call.answer("xatolik!!", show_alert=True)

