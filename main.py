a = 2
import datetime
import pytz
import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

from default import startbut, keldi_xd, ketdi_xd

from datetime import datetime

import datetime

import pytz
import openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

# set the timezone
tzInfo = pytz.timezone('Asia/Tashkent')
dt = datetime.datetime.now(tz=tzInfo)
developers_column = []
SHETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF']
path = "yanvar.xlsx"

# set the timezone

ADMINSS = [5172746353, 328628941, 2111796525, 233029021]

next_step = ["ariza_yoz", "exit"]


# clean
class MyStates(StatesGroup):
    next_step = State()
    ketdi_steep = State()
    adminka = State()
    capt = State()


userr = []
ndt_users_dict = {1207474771: "Yo`ldoshev Bobur",
                  233029021: "Karimov Anvar",
                  10414033: "Tulaboyev Zafar",
                  2111796525: "Sabina Sobirova",
                  328628941: "Quranboyev Jasur",
                  5172746353: "Sharifjon Mo`minov",
                  520754113: 'Shanazarov Abdullo',
                  524697244: 'Habibullayev Axtam',
                  322626456: 'Сматуллаев Ербол',
                  1336680858: 'Maxmudova Durdona',
                  1755017200: 'Nazaraliyev Jahongir'

                  }

API_TOKEN = '6110396068:AAFYfsw6Y0CAkyguzkLFwB-aHFKebC_1ca4'
XODIMLAR = [5172746353, 328628941, 1207474771, 233029021, 10414033, 2111796525, 520754113,
            524697244, 322626456, 1336680858, 1755017200]
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
x = datetime.datetime.now()


@dp.message_handler(commands=['ndtusers'])
async def send_welcome11(message: types.Message):
    a = []
    a.append(ndt_users_dict.values())
    for i in range(len(a)):
        await message.answer(a[i])
    a.clear()


# @dp.message_handler(commands=['up'])
# async def send_welcome4(message: types.Message):
#     await bot.send_message(328628941,
#                            f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[1755017200]}\n\n🕰<b>Vaqt</b>:  09:40:36-02/11/23 \n📍Manzil: 👇")
# 
#     await bot.send_message(5172746353,
#                            f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[1755017200]}\n\n🕰<b>Vaqt</b>:  09:40:36-02/11/23 \n📍Manzil: 👇")
# 

# @dp.message_handler(commands=['up'],content_type = types.ContentTypes.PHOTO)
# async def answer44(message: types.Message):
#     photo_id = message.photo[0].file_id
#     print(photo_id)
#     await bot.send_photo(5172746353, photo="C:/Users/momin/Desktop/ndt_new/photo_2023-02-09_12-42-08.jpg",caption="test")
# @dp.message_handler(commands=['up'])
# async def send_welcome4(message: types.Message):
#     photo  = "C:/Users/momin/Desktop/ndt_new/mm.jpg"
#     await bot.send_photo(5172746353,photo,caption="testing")

@dp.message_handler(commands=['support_admin'])
async def send_photo(message: types.Message):
    await message.answer("Rasmni Jo`nating!")
    await MyStates.adminka.set()
    # photo = "https://cdn.discordapp.com/attachments/989739840067207219/1073146412436557844/kingcs007_The_picture_of_the_employee_working_in_the_office_and_07356e0e-d41b-47a6-a3f0-e55be832cd30.png"
    # for i in range(len(XODIMLAR)):
    #     await bot.send_photo(XODIMLAR[i],photo,caption=f"""{}


# """)
@dp.message_handler(state=MyStates.adminka, content_types=types.ContentTypes.PHOTO)
async def ups(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    await MyStates.capt.set()
    await message.answer("Rasm qabul qilindi!\n\nRasm uchun text kiriting!")
    await state.finish()
    await MyStates.capt.set()
    print("kaptga zapros bordi")

    @dp.message_handler(state=MyStates.capt, content_types=types.ContentTypes.TEXT)
    async def ool(message: types.Message, state: FSMContext):
        print("capt ga kirdi")
        c = message.text
        await message.answer("Rasm uchun text kiriting!")
        for i in range(len(XODIMLAR)):
            await bot.send_photo(XODIMLAR[i], photo, caption=c)
        await state.finish()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global user_idtelegram
    xodim_id = message.from_user.id
    await message.answer(
        f"Salom,<b> {message.from_user.full_name}</b>")
    if xodim_id in ADMINSS and XODIMLAR:
        await message.answer("Sizning darajangiz Admin", reply_markup=startbut)
    if xodim_id in XODIMLAR:
        await message.answer(f"<b>{ndt_users_dict[xodim_id]}</b> siz xodimlar bo`limidan foydalana olasiz",
                             reply_markup=startbut)
    if xodim_id not in XODIMLAR:
        await message.answer("Siz bu botdan foydalanishga ruxsat etilmagansiz ❎")


@dp.message_handler(text="Xodim🧑‍💻")
async def sharif(message: types.Message):
    if message.from_user.id in XODIMLAR or ADMINSS:
        await message.answer("🛎 YOQLAMA 🛎", reply_markup=keldi_xd)
    else:
        await message.answer("Botda siz uchun lavozim ajratilmagan !")


@dp.message_handler(state=MyStates.ketdi_steep, content_types=types.ContentTypes.LOCATION)
async def ups(message: types.Message, state: FSMContext):
    await message.forward(233029021, message.message_id, message.chat.id)
    await bot.send_message(233029021,
                           f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[message.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    # PRAEKT MANAGER ADD
    await bot.send_message(328628941,
                           f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[message.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    await message.forward(328628941, message.message_id, message.chat.id)
    await message.forward(2111796525, message.message_id, message.chat.id)
    await bot.send_message(2111796525,
                           f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[message.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")

    await message.answer("Xayr 👋")
    await message.answer("Yangi ish kuniga kech qolmasdan keling 😊")
    await message.answer("Yangi ish kunini Boshlash !", reply_markup=keldi_xd)
    await state.finish()


@dp.message_handler(text="KELDI 🏢")
async def qoshish(message: types.Message):
    await message.answer("<b>Assalomu Aleykum</b> 😊\nBugungi ishda omad yor bo`lsin.")
    await message.answer("<b>Manzilni Jo`nating!</b>", reply_markup=ketdi_xd)
    await MyStates.next_step.set()


@dp.message_handler(state=MyStates.next_step, content_types=types.ContentTypes.LOCATION)
async def ups(message: types.Message, state: FSMContext):
    print("kirildi fsm ga")
    await message.answer("📍Manzilingiz Jo`natildi")
    await message.answer("<b>Ish vaqtini yakunlash!💫</b>", reply_markup=ketdi_xd)

    await bot.send_message(2111796525,
                           f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    await message.forward(2111796525, message.message_id, message.chat.id)
    await bot.send_message(328628941,
                           f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    await message.forward(328628941, message.message_id, message.chat.id)

    await bot.send_message(233029021,
                           f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    await message.forward(233029021, message.message_id, message.chat.id)

    wb_obj = openpyxl.load_workbook(path)

    sheet_obj = wb_obj.active

    max_col = sheet_obj.max_column

    ndt_users_dict = {1207474771: "Yo`ldoshev Bobur",
                      233029021: "Karimov Anvar",
                      10414033: "Tulaboyev Zafar",
                      2111796525: "Sabina Sobirova",
                      328628941: "Quranboyev Jasur",
                      5172746353: "Sharifjon Mo`minov",
                      520754113: 'Shanazarov Abdullo',
                      524697244: 'Habibullayev Axtam',
                      322626456: 'Сматуллаев Ербол',
                      1336680858: 'Maxmudova Durdona',
                      1755017200: 'Nazaraliyev Jahongir'

                      }

    x = datetime.datetime.now()

    o = 0
    a = x.strftime("%d")

    o += 1
    for jump in range(10):
        for i in range(1, max_col + 1):
            cell_obj = sheet_obj.cell(row=jump + 1, column=i)
            developers_column.append(cell_obj.value)

        for k in range(32):
            ws[f'{SHETS[k]}{jump + 1}'] = developers_column[k]
            print(developers_column[k])
        developers_column.clear()

    await state.finish()

@dp.message_handler(commands='oy_malumotlari')
async def excel_sender(messtage: types.Message):
    ex = open('sample.xlsx','rb')
    await bot.send_document(messtage.from_user.id,document=ex,caption='🏢Next Developers Team')


@dp.message_handler(text="KETDI 🏢")
async def qoshish(message: types.Message):
    await message.answer("Manzilni Tasdiqlang 📍", reply_markup=keldi_xd)
    await MyStates.ketdi_steep.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
