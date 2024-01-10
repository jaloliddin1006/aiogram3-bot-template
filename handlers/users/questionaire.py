from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Form
from keyboards import builders, reply
from filters import IsPrivateChat

router = Router()
router.message.filter(IsPrivateChat())


@router.message(Command('profile'))
async def profile_get(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer('Ismingizni kiriting: ', reply_markup=builders.profile(message.from_user.full_name))
    
    
@router.message(Form.name)
async def profile_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer('Yoshingizni kiriting: ', reply_markup=reply.rmk)

@router.message(Form.age)
async def profile_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Form.sex)
        await message.answer('Jinsingizni kiriting: ', reply_markup=builders.profile(["erkak", "ayol"]))
    else:
        await message.answer('Yoshingizni raqamda kiriting: ')

# @router.message(Form.sex, F.text.lower().one_of(['erkak', 'ayol']))     
@router.message(Form.sex, F.text.casefold().in_(['erkak', 'ayol']))  
async def profile_sex(message: Message, state: FSMContext):
    await state.update_data(sex = message.text)
    await state.set_state(Form.about)
    await message.answer("O'zigiz haqingizda nimadir yozing...", reply_markup=reply.rmk)
    
@router.message(Form.sex)  
async def notugri_profile_sex(message: Message, state: FSMContext):
    await message.answer("Knopkalardan birini tanlang")
    
    
@router.message(Form.about)
async def profile_about(message: Message, state: FSMContext):
    if len(message.text.split(' ')) > 5:
        await state.update_data(about = message.text) 
        await state.set_state(Form.photo)
        await message.answer("Reasmingizni yuboring...")
    else: 
        await message.answer("Kamida 5 ta so'z kiriting...")
        
        
@router.message(Form.photo, F.photo)
async def profile(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()
    
    formatted_txt = []
    [
        formatted_txt.append(f"{key}: {value}") for key, value in data.items()
    ]
    
    await message.answer_photo(
        photo_file_id,
        "\n".join(formatted_txt)
    )
    
    
@router.message(Form.photo, ~F.photo)
async def profile(message: Message, state: FSMContext):
    await message.answer("Faqat rasm yuboring")