import telebot
from telebot import types

bot = telebot.TeleBot('7401092703:AAEUIl1C1Q7UGDuV6C90OUyNrDuzhfks16I')

def inline1():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    class1 = types.InlineKeyboardButton("Бюджет", callback_data='Бюджет')
    class2 = types.InlineKeyboardButton("Премиум", callback_data='Премиум')
    class3 = types.InlineKeyboardButton("Люкс", callback_data='Люкс')
    kbd.add(class1, class2, class3)
    return kbd

def inline1m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Dacia", callback_data='Dacia')
    marka2 = types.InlineKeyboardButton("Datsun", callback_data='Datsun')
    marka3 = types.InlineKeyboardButton("Lada", callback_data='Lada')
    marka4 = types.InlineKeyboardButton("Kia", callback_data='Kia')
    back = types.InlineKeyboardButton("(назад)", callback_data='(назад)')
    kbd.add(marka1, marka2, marka3, marka4, back)
    return kbd

def inline2m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Volkswagen", callback_data='Volkswagen')
    marka2 = types.InlineKeyboardButton("BMW", callback_data='BMW')
    marka3 = types.InlineKeyboardButton("Cadillac", callback_data='Cadillac')
    marka4 = types.InlineKeyboardButton("Lexus", callback_data='Lexus')
    marka5 = types.InlineKeyboardButton("Jaguar", callback_data='Jaguar')
    back = types.InlineKeyboardButton("(назад)", callback_data='(назад)')
    kbd.add(marka1, marka2, marka3, marka4, marka5, back)
    return kbd

def inline3m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Rolls-Royce", callback_data='Rolls-Royce')
    marka2 = types.InlineKeyboardButton("Bentley", callback_data='Bentley')
    marka3 = types.InlineKeyboardButton("Bugatti", callback_data='Bugatti')
    marka4 = types.InlineKeyboardButton("Maybach", callback_data='Maybach')
    back = types.InlineKeyboardButton("(назад)", callback_data='(назад)')
    kbd.add(marka1, marka2, marka3, marka4, back)
    return kbd


#Для кнопки (назад)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'Бюджет':
        bot.send_message(call.message.chat.id, "Вы выбрали Бюджет.", reply_markup=inline1m())
    elif call.data == 'Премиум':
        bot.send_message(call.message.chat.id, "Вы выбрали Премиум.", reply_markup=inline2m())
    elif call.data == 'Люкс':
        bot.send_message(call.message.chat.id, "Вы выбрали Люкс.", reply_markup=inline3m())
    elif call.data in ['Dacia', 'Datsun', 'Lada', 'Kia']:
        bot.send_message(call.message.chat.id, "Вы выбрали марку " + call.data)

    elif call.data == 'Bentley':
        name = 'Bentley Bentayga, 2021'
        color = 'Цвет:  Синий'
        cash = '25.000.000 ₽'
        year = 'Год выпуска:  2021'
        probeg = '55.000 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель  4.0 л / 550 л.с. / Бензин'
        kuzov = 'Кузов  Внедорожник 5 дв.'
        privod = 'Привод  Полный'
        sost = 'Состояние не требуется ремонта'
        pts = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/bentley/bentayga/1124675566-61e69c1f/', parse_mode='html')

        name2 = 'Bentley Bentayga, 2024'
        color2 = 'Цвет:  Белый'
        cash2 = '32.900.000 ₽'
        year2 = 'Год выпуска:  2024'
        probeg2 = '100 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель  4.0 л / 550 л.с. / Бензин'
        kuzov2 = 'Кузов  Внедорожник 5 дв.'
        privod2 = 'Привод  Полный'
        sost2 = 'Состояние не требуется ремонта'
        pts2 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/bentley/bentayga/1124564356-8ae5920c/',parse_mode='html')

        name3 = 'Bentley Bentayga EWB, 2023'
        color3 = 'Цвет:  Сервый'
        cash3 = '49.282.600 ₽'
        year3 = 'Год выпуска:  2023'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель  4.0 л / 550 л.с. / Бензин'
        kuzov3 = 'Кузов  Внедорожник 5 дв.'
        privod3 = 'Привод  Полный'
        sost3 = 'Состояние не требуется ремонта'
        pts3 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/new/group/bentley/bentayga/23271554/22544511/1119893898-64c45a7f/',parse_mode='html')

    elif call.data == 'Bugatti':
        name = 'Bugatti Chiron, 2021'
        color = 'Цвет:  Синий'
        cash = '400.000.000 ₽'
        year = 'Год выпуска:  2021'
        probeg = '1 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель  8.0 л / 1500 л.с. / Бензин'
        kuzov = 'Кузов  Купе'
        privod = 'Привод  Полный'
        sost = 'Состояние не требуется ремонта'
        pts = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/bugatti/chiron/1124292308-a01c32ca/',parse_mode='html')

        name2 = 'Bugatti Chiron, 2021'
        color2 = 'Цвет:  Серебристый'
        cash2 = '410.000.000 ₽'
        year2 = 'Год выпуска:  2021'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель  8.0 л / 1500 л.с. / Бензин'
        kuzov2 = 'Кузов  Купе'
        privod2 = 'Привод  Полный'
        sost2 = 'Состояние не требуется ремонта'
        pts2 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/new/group/bugatti/chiron/20765749/21527797/1125055271-517065a1/',parse_mode='html')

        name3 = 'Bugatti Chiron, 2021'
        color3 = 'Цвет:  Белый'
        cash3 = '420.000.000 ₽'
        year3 = 'Год выпуска:  2021'
        probeg3 = '595 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель  8.0 л / 1500 л.с. / Бензин'
        kuzov3 = 'Кузов  Купе'
        privod3 = 'Привод  Полный'
        sost3 = 'Состояние не требуется ремонта'
        pts3 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/bugatti/chiron/1124215250-eb71b0d8/',parse_mode='html')

    elif call.data == 'Rolls-Royce':
        name = 'Rolls-Royce Cullinan Series II Black Badge, 2024'
        color = 'Цвет:  Чёрный'
        cash = '64.900.000 ₽'
        year = 'Год выпуска:  2024'
        probeg = '100 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель  6.8 л / 600 л.с. / Бензин'
        kuzov = 'Кузов  Внедорожник 5 дв.'
        privod = 'Привод  Полный'
        sost = 'Состояние не требуется ремонта'
        pts = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/rolls_royce/cullinan/1125451931-e193f62b/',parse_mode='html')

        name2 = 'Rolls-Royce Cullinan Series II Black Badge, 2024'
        color2 = 'Цвет:  Белый'
        cash2 = '62.500.000 ₽'
        year2 = 'Год выпуска:  2024'
        probeg2 = '39 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель  6.8 л / 600 л.с. / Бензин'
        kuzov2 = 'Кузлов  Внедорожник 5 дв.'
        privod2 = 'Привод  Полный'
        sost2 = 'Состояние не требуется ремонта'
        pts2 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/rolls_royce/cullinan/1125451579-4d2cc40a/',parse_mode='html')

        name3 = 'Rolls-Royce Spectre, 2023'
        color3 = 'Цвет:  Чёрный'
        cash3 = '84.933.800 ₽'
        year3 = 'Год выпуска:  2023'
        probeg3 = '530 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель  585 л.с. / 430 кВт / электро'
        kuzov3 = 'Кузов  Внедорожник 5 дв.'
        privod3 = 'Привод  Полный'
        sost3 = 'Состояние не требуется ремонта'
        pts3 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/new/group/rolls_royce/spectre/23403556/23804614/1124296284-edff7aed/',parse_mode='html')

    elif call.data == 'Maybach':
        name = 'Mercedes-Benz Maybach S-класс 4.0 AT, 2022'
        color = 'Цвет:  Чёрный'
        cash = '28.750.000 ₽'
        year = 'Год выпуска:  2022'
        probeg = '4.900 км'
        have = 'В НАЛИЧИИ'
        engine = 'Объём двигатель  4 л / Бензин'
        kuzov = 'Кузов  Седан'
        privod = 'Привод  Полный'
        sost = 'Состояние не требуется ремонта'
        pts = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://www.avito.ru/moskva/avtomobili/mercedes-benz_maybach_s-klass_4.0_at_2022_4_900_km_4801548844',parse_mode='html')

        name2 = 'Mercedes-Benz Maybach S-класс 4.0 AT, 2024'
        color2 = 'Цвет:  Чёрный'
        cash2 = '36.700.000 ₽'
        year2 = 'Год выпуска:  2024'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Объём двигатель  4 л / Бензин'
        kuzov2 = 'Кузов  Седан'
        privod2 = 'Привод  Полный'
        sost2 = 'Состояние не требуется ремонта'
        pts2 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://www.avito.ru/moskva/avtomobili/mercedes-benz_maybach_s-klass_4.0_at_2024_4271695103',parse_mode='html')

        name3 = 'Mercedes-Benz Maybach S-класс 4.0 AT, 2021'
        color3 = 'Цвет:  Чёрный'
        cash3 = '19.500.000 ₽'
        year3 = 'Год выпуска:  2021'
        probeg3 = '63.500 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Объём двигатель  4 л / Бензин'
        kuzov3 = 'Кузов  Седан'
        privod3 = 'Привод  Электронный'
        sost3 = 'Состояние не требуется ремонта'
        pts3 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://www.avito.ru/moskva/avtomobili/mercedes-benz_maybach_s-klass_4.0_at_2021_63_500_km_4556343769',parse_mode='html')

    # ===========
    elif call.data in ['Volkswagen', 'BMW', 'Cadillac', 'Lexus', 'Jaguar']:
        bot.send_message(call.message.chat.id, "Вы выбрали марку " + call.data)
    elif call.data == '(назад)':
        bot.send_message(call.message.chat.id, "Вы вернулись назад в меню выбора.", reply_markup=inline1())

# ========= СКРИПТ СООБЩЕНИЯ ОТ БОТА =========
@bot.message_handler(commands=['start'])
def start(message):
    firtword = 'Это телеграмм бот, который поможет вам найти идеальный автомобиль! 🚗'
    secword = 'Как это работает:\n- Выберете нужные вам параметры: бюджет, марка.\n- Получите персонализированные рекомендации на основе ваших запросов.'
    threeword = 'Почему именно этот бот?\n- Мгновенная база данных с актуальными предложениями.\n- Удобный и простой интерфейс для быстрого поиска.'
    fourword = 'Начните прямо сейчас!\nПросто выберете нужные параметры и получите список автомобилей, которые идеально подойдут вам. Наш бот сделает процесс поиска простым и быстрым!'

    bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b>!", parse_mode='html')
    bot.send_message(message.chat.id, f"{firtword}\n\n{secword}\n\n{threeword}\n\n{fourword}", parse_mode='html', reply_markup=inline1())

@bot.callback_query_handler(func=lambda call: True)
def call_query(call):
    if call.message:
        if call.data == 'Бюджет':
            bot.send_message(call.message.chat.id, "Выберите марку автомобиля", reply_markup=inline1m())
        if call.data == 'Премиум':
            bot.send_message(call.message.chat.id, "Выберите марку автомобиля", reply_markup=inline2m())
        if call.data == 'Люкс':
            bot.send_message(call.message.chat.id, 'Выберите марку автомобиля',reply_markup=inline3m())

        bot.answer_callback_query(callback_query_id=call.id, show_alert=False)

    bot.delete_message(call.message.chat.id, call.message.message_id) #удаление предыдущего сообщения

bot.polling(none_stop=True)