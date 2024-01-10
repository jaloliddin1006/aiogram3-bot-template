from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def calc_kb():
    items = [
        "1", "2", "3", "+",
        "4", "5", "6", "-",
        "7", "8", "9", "*",
        "0", ".", "=", "/"
    ]
    
    builder = ReplyKeyboardBuilder()
    [builder.button(text=item) for item in items]
    
    builder.button(text="Orqaga")
    builder.adjust(*[4]*4, 1) # 4, 4, 4, 4, 1
    
    return builder.as_markup(resize_keyboard=True)


def profile(text: str | list):
    builder = ReplyKeyboardBuilder()
    if isinstance(text, str):
        text = [text]
    [builder.button(text=item) for item in text]
    
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
        
        
def check_channel_sub(chanells: list):
    builder = InlineKeyboardBuilder()
    [builder.button(text=name, url=link) for name, link in chanells]
    return builder.as_markup()