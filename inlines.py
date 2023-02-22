from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import datetime

ndt_users_dict = {1207474771: "Yo`ldoshev Bobur",
                  233029021: "Karimov Anvar",
                  10414033: "Tulaboyev Zafar",
                  2111796525: "Sobirova Sabina",
                  328628941: "Quranboyev Jasur",
                  5172746353: "Mo`minov Sharifjon",
                  520754113: 'Shanazarov Abdullo',
                  524697244: 'Habibullayev Axtam',
                  322626456: 'Сматуллаев Ербол',
                  1336680858: 'Maxmudova Durdona',
                  1755017200: 'Nazaraliyev Jahongir'
                  }
ndt_usertable = InlineKeyboardMarkup(
    inline_keyboard=[
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[1207474771]}", callback_data="bobur"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[233029021]}", callback_data="zafar"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[10414033]}", callback_data="sabina"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[2111796525]}", callback_data="jasur"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[5172746353]}", callback_data="sharif"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[520754113]}", callback_data="abdullo"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[524697244]}", callback_data="axtam"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[322626456]}", callback_data="erbol"),
        ],
        [

            InlineKeyboardButton(text=f"{ndt_users_dict[1336680858]}", callback_data="durdona"),
        ],
        [
            InlineKeyboardButton(text=f"{ndt_users_dict[1755017200]}", callback_data="jahongir")
        ],

    ],
)

# ndt_usertable = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             [ InlineKeyboardButton(text=f"{ndt_users_dict[1207474771]}", callback_data="bobur"),
# ],
#          [   InlineKeyboardButton(text=f"{ndt_users_dict[233029021]}", callback_data="zafar")
# ],
#           [  InlineKeyboardButton(text=f"{ndt_users_dict[10414033]}", callback_data="sabina")
# ],
#            [ InlineKeyboardButton(text=f"{ndt_users_dict[2111796525]}", callback_data="jasur")
# ],
#            [ InlineKeyboardButton(text=f"{ndt_users_dict[5172746353]}", callback_data="sharif")
# ],
#          [   InlineKeyboardButton(text=f"{ndt_users_dict[520754113]}", callback_data="abdullo"),
# ],
#           [  InlineKeyboardButton(text=f"{ndt_users_dict[524697244]}", callback_data="axtam"),
# ],
#           [  InlineKeyboardButton(text=f"{ndt_users_dict[322626456]}", callback_data="erbol"),
# ],
#            [ InlineKeyboardButton(text=f"{ndt_users_dict[1336680858]}", callback_data="durdona"),
# ],
#             InlineKeyboardButton(text=f"{ndt_users_dict[1755017200]}", callback_data="jahongir"),
#         ],
#
#     ],
# )
import datetime

x = datetime.datetime.now()

adminka = InlineKeyboardMarkup(
    inline_keyboard=[
        [

            InlineKeyboardButton(text=f'📆{x.strftime("%B")} monitoring', callback_data="month"),
            InlineKeyboardButton(text=f'📆7 Kun monitoringi', callback_data="week")

        ],

    ],
)
