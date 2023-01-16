from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startbut = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xodim🧑‍💻"),
        ],

    ],
    resize_keyboard=True,
)
locat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzilni Tasdiqlash 📍", request_location=True),
        ],

    ],
    resize_keyboard=True,
)
