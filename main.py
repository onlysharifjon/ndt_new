import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from default import startbut, keldi_xd, ketdi_xd, all_info
from datetime import datetime
from inlines import adminka, ndt_usertable
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
SHETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF']
path = "monitoring.xlsx"
# admin ndt users
ADMINSS = [5172746353, 328628941, 2111796525, 233029021]


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

a = []


@dp.message_handler(commands=['ndtusers'])
async def send_welcome11(message: types.Message):
    a.append(ndt_users_dict.values())
    for i in range(len(a)):
        await message.answer(a[i])
    a.clear()


"""-----------------------------------------------------------------------adminka-----------------------------------------------------------------"""


@dp.message_handler(commands=['admin'])
async def send_welcome41(message: types.Message):
    await message.delete()
    await message.answer("Menu Admin", reply_markup=adminka)

    @dp.callback_query_handler(text=["month"])
    async def answer1(call: CallbackQuery):
        await call.message.delete()

        ex = open('monitoring.xlsx', 'rb')
        await call.bot.send_document(message.from_user.id, document=ex, caption='🏢Next Developers Team')

    @dp.callback_query_handler(text=["week"])
    async def answer2(call: CallbackQuery):
        await call.message.delete()

        await call.message.answer("<b>🧑‍💻Xodimlar ro'yxati</b>", reply_markup=ndt_usertable)
        await message.answer("⬇️Barcha Xodimlar Ma`lumotlarini ko`rish⬇️", reply_markup=all_info)


@dp.message_handler(text="📃Barcha xodimlar monitoringi (7 kun)")
async def infos_all(message: types.Message):
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column

    for saver in range(32):
        ws.column_dimensions[f'{SHETS[saver]}'].width = 28
    ws.column_dimensions[f'A'].width = 23
    a = x.strftime("%d")
    for jump in range(8):
        for i in range(1, max_col + 1):
            cell_obj = sheet_obj.cell(row=jump + 2, column=i)
            developers_column.append(cell_obj.value)
        # print(developers_column)
        if int(a) >= 7:
            monit_list = []
            for o in range(7):
                # print(int(a) - 6 + o)
                if developers_column[int(a) - 6 + o] != '.':
                    monit_list.append(developers_column[int(a) - 6 + o])
                else:
                    monit_list.append("❌")
            await message.answer(f"""
<b>Xodim: {developers_column[0]} </b>

<b>{int(a) - 6}:</b> {monit_list[0]}

<b>{int(a) - 5}:</b>  {monit_list[1]}

<b>{int(a) - 4}:</b> {monit_list[2]}

<b>{int(a) - 3}:</b> {monit_list[3]}

<b>{int(a) - 2}:</b> {monit_list[4]}

<b>{int(a) - 1}:</b> {monit_list[5]}

<b>{int(a)}:</b> {monit_list[6]}
""")
            monit_list.clear()
            developers_column.clear()
        else:
            await message.answer("⏳7 kun ma`lumoti mavjud emas\n\n🕥Bugun Sana")

@dp.callback_query_handler(text=["sharif"])
async def answer2(call: CallbackQuery):
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    x = datetime.datetime.now()

    o = 0
    a = x.strftime("%d")
    text = ""
    for jump in range(9):
        for i in range(1, max_col + 1):
            cell_obj = sheet_obj.cell(row=jump + 1, column=i)
            developers_column.append(cell_obj.value)
        # print("salom")
        print(developers_column)
        if developers_column[0] == ndt_users_dict[5172746353]:
            if int(a) >= 7:
                monit_list = []
                for o in range(7):
                    # print(int(a) - 6 + o)
                    if developers_column[int(a) - 6 + o] != '.':
                        monit_list.append(developers_column[int(a) - 6 + o])
                    else:
                        monit_list.append("❌")
                await call.message.answer(f"""
            <b>Xodim: {developers_column[0]} </b>

            <b>{int(a) - 6}:</b> {monit_list[0]}

            <b>{int(a) - 5}:</b>  {monit_list[1]}

            <b>{int(a) - 4}:</b> {monit_list[2]}

            <b>{int(a) - 3}:</b> {monit_list[3]}

            <b>{int(a) - 2}:</b> {monit_list[4]}

            <b>{int(a) - 1}:</b> {monit_list[5]}

            <b>{int(a)}:</b> {monit_list[6]}
            """)
                monit_list.clear()

            else:
                await call.message.answer("⏳7 kun ma`lumoti mavjud emas\n\n🕥Bugun Sana")
        developers_column.clear()
        # print(f"uz {text}")



"""-----------------------------------------------------------------------adminka-----------------------------------------------------------------"""


@dp.message_handler(commands=['support_admin'])
async def send_photo(message: types.Message):
    await message.answer("Rasmni Jo`nating!")
    await MyStates.adminka.set()


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
    # await message.forward(233029021, message.message_id, message.chat.id)
    # await bot.send_message(233029021,
    #                        f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[message.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    # # anvar akaga send qilish
    # await bot.send_message(328628941,
    #                        f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[message.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    # await message.forward(328628941, message.message_id, message.chat.id)
    # # jasur akaga send qilish
    # await message.forward(2111796525, message.message_id, message.chat.id)
    # await bot.send_message(2111796525,
    #                        f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[message.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    # sabinaga send qilish
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    x = datetime.datetime.now()
    for saver in range(32):
        ws.column_dimensions[f'{SHETS[saver]}'].width = 28
    ws.column_dimensions[f'A'].width = 23
    a = x.strftime("%d")
    for jump in range(9):
        for i in range(1, max_col + 1):
            cell_obj = sheet_obj.cell(row=jump + 1, column=i)
            developers_column.append(cell_obj.value)
        # print(developers_column)
        if developers_column[0] == ndt_users_dict[message.from_user.id]:
            editer = developers_column[int(a)]
            print(developers_column)
            developers_column[int(a)] = f"""Keldi: {editer} Ketdi: {str(x.strftime("%X"))}"""
        for k in range(32):
            ws[f'{SHETS[k]}{jump + 1}'] = developers_column[k]
            # print(developers_column[k])
        developers_column.clear()
    wb.save("monitoring.xlsx")
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
    # await bot.send_message(233029021,
    #                        f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    # await message.forward(233029021, message.message_id, message.chat.id)
    # #anvar akaga send qilish
    #
    #
    # await bot.send_message(2111796525,
    #                        f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    # await message.forward(2111796525, message.message_id, message.chat.id)
    # #sabina opaga send qilish
    #
    # await bot.send_message(328628941,
    #                        f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    # await message.forward(328628941, message.message_id, message.chat.id)
    # #jasur aka ga send qilish
    wb_obj = openpyxl.load_workbook(path)
    sheet_obj = wb_obj.active
    max_col = sheet_obj.max_column
    x = datetime.datetime.now()

    o = 0
    a = x.strftime("%d")
    for jump in range(9):
        for i in range(1, max_col + 1):
            cell_obj = sheet_obj.cell(row=jump + 1, column=i)
            developers_column.append(cell_obj.value)
        # print(developers_column)
        if developers_column[0] == ndt_users_dict[message.from_user.id]:
            developers_column[int(a)] = str(x.strftime("%X"))
        for k in range(32):
            ws[f'{SHETS[k]}{jump + 1}'] = developers_column[k]
            # print(developers_column[k])
        developers_column.clear()
    for saver in range(32):
        ws.column_dimensions[f'{SHETS[saver]}'].width = 28
    ws.column_dimensions[f'A'].width = 23
    wb.save("monitoring.xlsx")
    await state.finish()


@dp.message_handler(commands='oy_malumotlari')
async def excel_sender(messtage: types.Message):
    ex = open('monitoring.xlsx', 'rb')
    await bot.send_document(messtage.from_user.id, document=ex, caption='🏢Next Developers Team')
    # praekt manager send meesage forvard indfo


@dp.message_handler(text="KETDI 🏢")
async def qoshish(message: types.Message):
    await message.answer("Manzilni Tasdiqlang 📍", reply_markup=keldi_xd)
    await MyStates.ketdi_steep.set()
    #         # print(developers_column)
    #         # print("developer column 0")
    #         text+=str(f'Xodim: {ndt_users_dict[5172746353]}\n')
    #         for month in range(len(developers_column)-2):
    #             if len(str(developers_column[month]))<2:
    #                 text += f"<b>{month + 1}: </b>❌\n"
    #                 print(f'{month}----------------------------------------------')
    #             elif developers_column[month] != '.':
    #                 # print(developers_column[month])
    #                 text+=f"<b>{month+1}:</b> {developers_column[month+2]}\n"
    #                 # print(developers_column[month+2])
    #
    #             else:
    #                 print(f'{month}-----------')
    #                 text+=f"<b>{month+1}: </b>❌\n"
    #     developers_column.clear()
    # # await call.message.delete()
    # # print("Start text")
    # # print(text)
    # await call.message.answer(f"{text}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
