from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startbut = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Xodim🧑‍💻"),
        ],

    ],
    resize_keyboard=True,
)
ketdi_xd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="KETDI 🏢"),
            KeyboardButton(text="Manzilni Tasdiqlash 📍", request_location=True),



        ],

    ],
    resize_keyboard=True,
)
keldi_xd = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="KELDI 🏢"),
            KeyboardButton(text="Manzilni Tasdiqlash 📍", request_location=True),

        ],

    ],
    resize_keyboard=True,
)
import datetime
import pytz

#set the timezone
tzInfo = pytz.timezone('Asia/Tashkent')
dt = datetime.datetime.now(tz=tzInfo)
print(dt)