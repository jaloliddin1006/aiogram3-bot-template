from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    KeyboardButtonPollType,
    ReplyKeyboardRemove
)


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="smayliki"),
            KeyboardButton(text="ssilki")
        ],
        [
            KeyboardButton(text="calculator"),
            KeyboardButton(text="maxsus btn")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Biror birini tanlang",
    selective=True

)



maxsus_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="location", request_location=True),
            KeyboardButton(text="contact", request_contact=True),
        ],
        [
            KeyboardButton(text=" poll", request_poll=KeyboardButtonPollType()),
        ],
        [
            KeyboardButton(text="Orqaga")
            
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

rmk = ReplyKeyboardRemove()