import datetime
import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery

from default import startbut, locat
from inlines import yoqlama1, yoqlama2

ADMINSS = [5172746353, 328628941,2111796525]

next_step = ["ariza_yoz", "exit"]


class MyStates(StatesGroup):
    next_step = State()


# @dp.message_handler(state = NameStates.name_step, content_types = types.ContentTypes.TEXT)
# async def ups(message: types.Message, state: FSMContext):
#     if message.text == "Orqaga🔙":
#         await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
#         await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup = xodimlar)
#         await NameStates.name_step.set()
#     else:
#         names = message.text
#         d.append(names)
#         await message.answer("👥Familyangizni kiriting !")
#         await state.finish()
#         await NameStates.familiya.set()

API_TOKEN = '5428656747:AAEBNyZiMxyEzoze8XxrRLpbKNL0jeRfY3M'
XODIMLAR = [5172746353, 328628941, 1207474771, 233029021, 49257001, 10414033, 2111796525, 856306959]
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
x = datetime.datetime.now()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    ndt_users_dict = {1207474771: "Yo`ldoshev Bobur",
                      # 233029021: "Karimov Anvar",
                      49257001: "Umarjonov Ulug'bek",
                      10414033: "Tulaboyev Zafar",
                      2111796525: "Sabina Sobirovna",
                      328628941: "Quranboyev Jasur",
                      5172746353: "Sharifjon Mo`minov",
                      856306959: 'Umarxonov Azamxon',
                      520754113: 'Shanazarov Abdullo',
                      524697244: 'Habibullayev Axtam',
                      322626456: 'Сматуллаев Ербол'
                      }
    global user_idtelegram
    xodim_id = message.from_user.id
    await message.answer(
        f"Salom,<b> {message.from_user.full_name}</b>", reply_markup=startbut)
    if xodim_id in ADMINSS and XODIMLAR:
        await message.answer("Sizning darajangiz Admin")
    elif xodim_id in XODIMLAR:
        await message.answer(f"<b>{ndt_users_dict[xodim_id]}</b> siz xodimlar bo`limidan foydalana olasiz")

    else:
        await message.answer("Siz bu botdan foydalanishga ruxsat etilmagansiz ❎")


@dp.message_handler(text="Xodim🧑‍💻")
async def sharif(message: types.Message):
    if message.from_user.id in XODIMLAR or ADMINSS:
        await message.answer("🛎 YOQLAMA 🛎", reply_markup=yoqlama1)
    else:
        await message.answer("Botda siz uchun lavozim ajratilmagan !")


@dp.callback_query_handler(text="keldi")
async def qoshish(call: CallbackQuery):
    ndt_users_dict = {1207474771: "Yo`ldoshev Bobur",
                      # 233029021: "Karimov Anvar",
                      49257001: "Umarjonov Ulug'bek",
                      10414033: "Tulaboyev Zafar",
                      2111796525: "Sabina Sobirovna",
                      328628941: "Quranboyev Jasur",
                      5172746353: "Sharifjon Mo`minov",
                      856306959: 'Umarxonov Azamxon',
                      520754113: 'Shanazarov Abdullo',
                      524697244: 'Habibullayev Axtam',
                      322626456: 'Сматуллаев Ербол'
                      }
    await bot.send_message(2111796525,
                           f"💼<b> ISHGA KELDI</b>\n💼<b>Xodim</b>: {ndt_users_dict[call.from_user.id]}\n\n🕰<b>Vaqt</b>: {str(datetime.datetime.now().strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    await bot.send_message(328628941,
                           f"ISHGA KELDI\nXodim:{ndt_users_dict[call.from_user.id]}\n\nVaqt: {str(datetime.datetime.now().strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    await call.message.answer("<b>Assalomu Aleykum</b> 😊\nBugungi ishda omad yor bo`lsin.")
    await call.message.answer("<b>Manzilni Jo`nating!</b>", reply_markup=locat)
    await MyStates.next_step.set()


@dp.callback_query_handler(text="ketdi")
async def qoshish(call: CallbackQuery):
    ndt_users_dict = {1207474771: "Yo`ldoshev Bobur",
                      # 233029021: "Karimov Anvar",
                      49257001: "Umarjonov Ulug'bek",
                      10414033: "Tulaboyev Zafar",
                      2111796525: "Sabina Sobirovna",
                      328628941: "Quranboyev Jasur",
                      5172746353: "Sharifjon Mo`minov",
                      856306959: 'Umarxonov Azamxon',
                      520754113: 'Shanazarov Abdullo',
                      524697244: 'Habibullayev Axtam',
                      322626456: 'Сматуллаев Ербол'
                      }
    await call.message.answer("Xayr 👋")
    await bot.send_message(2111796525,
                           f"💼<b>Ish vaqti yakunladi !</b>\n💼Xodim: {ndt_users_dict[call.from_user.id]}\n\n🕰Vaqt: {str(datetime.datetime.now().strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")
    await bot.send_message(328628941,
                           f"ISHGA KELDI\nXodim:{ndt_users_dict[call.from_user.id]}\n\nVaqt: {str(datetime.datetime.now().strftime('%X'))}-{str(datetime.datetime.now().strftime('%x'))}")

@dp.message_handler(state = MyStates.next_step, content_types = types.ContentTypes.LOCATION)
async def ups(message: types.Message, state: FSMContext):
    print("kirildi fsm ga")
    await message.answer("Manzilingiz Jo`natildi")
    await message.answer("<b>Yangi ish kunini boshlash</b>", reply_markup=yoqlama1)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
