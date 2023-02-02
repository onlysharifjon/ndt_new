a = 1
import datetime
import pytz
import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery

from default import startbut, locat
from inlines import yoqlama1, yoqlama2

from datetime import datetime
import datetime
import pytz

# set the timezone
tzInfo = pytz.timezone('Asia/Tashkent')
dt = datetime.datetime.now(tz=tzInfo)
ADMINSS = [5172746353, 328628941, 2111796525, 233029021]

next_step = ["ariza_yoz", "exit"]


# clean
class MyStates(StatesGroup):
    next_step = State()
    ketdi_steep = State()


ndt_users_dict = {1207474771: "Yo`ldoshev Bobur",
                  233029021: "Karimov Anvar",
                  49257001: "Umarjonov Ulug'bek",
                  10414033: "Tulaboyev Zafar",
                  2111796525: "Sabina Sobirova",
                  328628941: "Quranboyev Jasur",
                  5172746353: "Sharifjon Mo`minov",
                  856306959: 'Umarxonov Azamxon',
                  520754113: 'Shanazarov Abdullo',
                  524697244: 'Habibullayev Axtam',
                  322626456: 'Сматуллаев Ербол',
                  1336680858: 'Maxmudova Durdona',
                  1755017200: 'Nazaraliyev Jahongir'

                  }

API_TOKEN = '5428656747:AAEBNyZiMxyEzoze8XxrRLpbKNL0jeRfY3M'
XODIMLAR = [5172746353, 328628941, 1207474771, 233029021, 49257001, 10414033, 2111796525, 856306959, 520754113,
            524697244, 322626456, 1336680858]
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
        await message.answer("🛎 YOQLAMA 🛎", reply_markup=yoqlama1)
    else:
        await message.answer("Botda siz uchun lavozim ajratilmagan !")


@dp.callback_query_handler(text="ketdi")
async def qoshish(call: CallbackQuery):
    await call.message.answer("Manzilni Tasdiqlang 📍", reply_markup=locat)
    await MyStates.ketdi_steep.set()

    await bot.send_message(2111796525,
                           f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[call.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    await bot.send_message(328628941,
                           f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[call.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    await bot.send_message(233029021,
                           f"🏘<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[call.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    #PRAEKT MANAGER ADD



@dp.message_handler(state=MyStates.ketdi_steep, content_types=types.ContentTypes.LOCATION)
async def ups(message: types.Message, state: FSMContext):
    await message.answer("Xayr 👋")
    await message.answer("Yangi ish kuniga kech qolmasdan keling 😊")
    await message.answer("Yangi ish kunini Boshlash !", reply_markup=yoqlama1)
    await state.finish()


@dp.callback_query_handler(text="keldi")
async def qoshish(call: CallbackQuery):
    await call.message.answer("<b>Assalomu Aleykum</b> 😊\nBugungi ishda omad yor bo`lsin.")
    await call.message.answer("<b>Manzilni Jo`nating!</b>", reply_markup=locat)
    await MyStates.next_step.set()


@dp.message_handler(state=MyStates.next_step, content_types=types.ContentTypes.LOCATION)
async def ups(message: types.Message, state: FSMContext):
    print("kirildi fsm ga")
    await message.answer("📍Manzilingiz Jo`natildi")
    await message.answer("<b>Ish vaqtini yakunlash!💫</b>", reply_markup=yoqlama2)

    await bot.send_message(2111796525,
                           f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    await message.forward(2111796525, message.message_id, message.chat.id)
    await bot.send_message(328628941,
                           f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    await message.forward(328628941, message.message_id, message.chat.id)

    await bot.send_message(233029021,
                           f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")
    await message.forward(233029021,message.message_id,message.chat.id)
    
    #praekt manager send meesage forvard indfo
    
    await bot.send_message(5172746353,
                           f"🏢<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[message.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now(tz=tzInfo).strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}\n📍Manzil: 👇")

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

