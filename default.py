from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startbut = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xodim๐งโ๐ป"),
        ],

    ],
    resize_keyboard=True,
)
all_info = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="๐Barcha xodimlar monitoringi (7 kun)"),
        ],

    ],
    resize_keyboard=True,
)
ketdi_xd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="KETDI ๐ข"),
            KeyboardButton(text="Manzilni Tasdiqlash ๐", request_location=True),



        ],

    ],
    resize_keyboard=True,
)
keldi_xd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="KELDI ๐ข"),
            KeyboardButton(text="Manzilni Tasdiqlash ๐", request_location=True),

        ],

    ],
    resize_keyboard=True,
)
