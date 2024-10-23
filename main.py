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
    marka1 = types.InlineKeyboardButton("Lada", callback_data='Lada')
    marka2 = types.InlineKeyboardButton("Kia", callback_data='Kia')
    marka3 = types.InlineKeyboardButton("Dacia", callback_data='Dacia')
    marka4 = types.InlineKeyboardButton("Datsun", callback_data='Datsun')
    back = types.InlineKeyboardButton("(назад)", callback_data='(назад)')
    kbd.add(marka1, marka2, marka3, marka4, back)
    return kbd

def inline2m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Volkswagen", callback_data='Volkswagen')
    marka2 = types.InlineKeyboardButton("BMW", callback_data='BMW')
    marka3 = types.InlineKeyboardButton("Audi", callback_data='Audi')
    marka4 = types.InlineKeyboardButton("Mazda", callback_data='Mazda')
    marka5 = types.InlineKeyboardButton("Lexus", callback_data='Lexus')
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
    #elif call.data in ['Dacia', 'Datsun', 'Lada', 'Kia']:
    #     bot.send_message(call.message.chat.id, "Вы выбрали марку " + call.data)

    elif call.data == 'Bentley':
        name = 'Bentley Bentayga, 2021'
        color = 'Цвет: Синий'
        cash = '25.000.000 ₽'
        year = 'Год выпуска: 2021'
        probeg = 'Пробег: 55.000 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 550 л.с. / 4.0 л / Бензин'
        kuzov = 'Кузов: Внедорожник 5 дв.'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/bentley/bentayga/1124675566-61e69c1f/', parse_mode='html')

        name2 = 'Bentley Bentayga, 2024'
        color2 = 'Цвет: Белый'
        cash2 = '32.900.000 ₽'
        year2 = 'Год выпуска: 2024'
        probeg2 = 'Пробег: 100 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 550 л.с. / 4.0 л / Бензин'
        kuzov2 = 'Кузов: Внедорожник 5 дв.'
        privod2 = 'Привод: Полный'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/bentley/bentayga/1124564356-8ae5920c/',parse_mode='html')

        name3 = 'Bentley Bentayga EWB, 2023'
        color3 = 'Цвет: Сервый'
        cash3 = '49.282.600 ₽'
        year3 = 'Год выпуска: 2023'
        probeg3 = 'Пробег: Без пробега'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 550 л.с. / 4.0 л / Бензин'
        kuzov3 = 'Кузов: Внедорожник 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/new/group/bentley/bentayga/23271554/22544511/1119893898-64c45a7f/',parse_mode='html')

    elif call.data == 'Bugatti':
        name = 'Bugatti Chiron, 2021'
        color = 'Цвет: Синий'
        cash = '400.000.000 ₽'
        year = 'Год выпуска: 2021'
        probeg = 'Пробег: 1 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 1500 л.с. / 8.0 л / Бензин'
        kuzov = 'Кузов: Купе'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/bugatti/chiron/1124292308-a01c32ca/',parse_mode='html')

        name2 = 'Bugatti Chiron, 2021'
        color2 = 'Цвет: Серебристый'
        cash2 = '410.000.000 ₽'
        year2 = 'Год выпуска: 2021'
        probeg2 = 'Пробег: Без пробега'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 1500 л.с. / 8.0 л / Бензин'
        kuzov2 = 'Кузов: Купе'
        privod2 = 'Привод: Полный'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/new/group/bugatti/chiron/20765749/21527797/1125055271-517065a1/',parse_mode='html')

        name3 = 'Bugatti Chiron, 2021'
        color3 = 'Цвет: Белый'
        cash3 = '420.000.000 ₽'
        year3 = 'Год выпуска: 2021'
        probeg3 = 'Пробег: 595 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 1500 л.с. / 8.0 л / Бензин'
        kuzov3 = 'Кузов: Купе'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/bugatti/chiron/1124215250-eb71b0d8/',parse_mode='html')

    elif call.data == 'Rolls-Royce':
        name = 'Rolls-Royce Cullinan Series II Black Badge, 2024'
        color = 'Цвет: Чёрный'
        cash = '64.900.000 ₽'
        year = 'Год выпуска: 2024'
        probeg = 'Пробег: 100 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 600 л.с. / 6.8 л / Бензин'
        kuzov = 'Кузов: Внедорожник 5 дв.'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/rolls_royce/cullinan/1125451931-e193f62b/',parse_mode='html')

        name2 = 'Rolls-Royce Cullinan Series II Black Badge, 2024'
        color2 = 'Цвет: Белый'
        cash2 = '62.500.000 ₽'
        year2 = 'Год выпуска: 2024'
        probeg2 = 'Пробег: 39 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 600 л.с. / 6.8 л / Бензин'
        kuzov2 = 'Кузлов: Внедорожник 5 дв.'
        privod2 = 'Привод: Полный'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/rolls_royce/cullinan/1125451579-4d2cc40a/',parse_mode='html')

        name3 = 'Rolls-Royce Spectre, 2023'
        color3 = 'Цвет: Чёрный'
        cash3 = '84.933.800 ₽'
        year3 = 'Год выпуска: 2023'
        probeg3 = 'Пробег: 530 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 585 л.с. / 430 кВт / Электро'
        kuzov3 = 'Кузов: Внедорожник 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/new/group/rolls_royce/spectre/23403556/23804614/1124296284-edff7aed/',parse_mode='html')

    elif call.data == 'Maybach':
        name = 'Mercedes-Benz Maybach S-класс 4.0 AT, 2022'
        color = 'Цвет: Чёрный'
        cash = '28.750.000 ₽'
        year = 'Год выпуска: 2022'
        probeg = 'Пробег: 4.900 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 503 л.с / 4 л / Бензин'
        kuzov = 'Кузов: Седан'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://www.avito.ru/moskva/avtomobili/mercedes-benz_maybach_s-klass_4.0_at_2022_4_900_km_4801548844',parse_mode='html')

        name2 = 'Mercedes-Benz Maybach S-класс 4.0 AT, 2024'
        color2 = 'Цвет:  Чёрный'
        cash2 = '36.700.000 ₽'
        year2 = 'Год выпуска:  2024'
        probeg2 = 'Пробег: Без пробега'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель  503 л.с / 4 л / Бензин'
        kuzov2 = 'Кузов  Седан'
        privod2 = 'Привод  Полный'
        sost2 = 'Состояние не требуется ремонта'
        pts2 = 'ПТС  Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://www.avito.ru/moskva/avtomobili/mercedes-benz_maybach_s-klass_4.0_at_2024_4271695103',parse_mode='html')

        name3 = 'Mercedes-Benz Maybach S-класс 4.0 AT, 2021'
        color3 = 'Цвет:  Чёрный'
        cash3 = '19.500.000 ₽'
        year3 = 'Год выпуска: 2021'
        probeg3 = 'Пробег: 63.500 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель  503 л.с / 4 л / Бензин'
        kuzov3 = 'Кузов: Седан'
        privod3 = 'Привод: Электронный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://www.avito.ru/moskva/avtomobili/mercedes-benz_maybach_s-klass_4.0_at_2021_63_500_km_4556343769',parse_mode='html')

    # ===========
    elif call.data == 'Volkswagen':
        name = 'Volkswagen ID.6 X, 2023'
        color = 'Цвет: Белый'
        cash = '5.400.000 ₽'
        year = 'Год выпуска: 2023'
        probeg = 'Пробег: Без пробега'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 230 л.с / 230 кВт / Электро'
        kuzov = 'Кузов: Внедорожник 5 дв.'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/new/group/volkswagen/id6/23178742/23661178/1123238228-550cb29d/', parse_mode='html')

        name2 = 'Volkswagen Tiguan L Pro, 2024'
        color2 = 'Цвет: Белый'
        cash2 = '6.700.000 ₽'
        year2 = 'Год выпуска: 2024'
        probeg2 = 'Пробег: Без пробега'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 220 л.с. / 2.9 л / Бензин'
        kuzov2 = 'Кузов: Внедорожник 5 дв.'
        privod2 = 'Привод: Полный'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/new/group/volkswagen/tiguan/23983358/23983446/1125378713-335070db/',parse_mode='html')

        name3 = 'Volkswagen Tayron, 2023'
        color3 = 'Цвет: Черный'
        cash3 = '5.463.000 ₽'
        year3 = 'Год выпуска: 2023'
        probeg3 = 'Пробег: Без пробега'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 220 л.с. / 2.0 л. / Бензин'
        kuzov3 = 'Кузов: Внедорожник 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/new/group/volkswagen/tayron/23415753/23695272/1123060914-d9bbcbdf/',parse_mode='html')


    elif call.data == 'BMW':
        name = 'BMW Z4 20i, 2019'
        color = 'Цвет: Черный'
        cash = '4.500.000 ₽'
        year = 'Год выпуска: 2019'
        probeg = 'Пробег: 45.000 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 197 л.с./ 2.0 л / Бензин'
        kuzov = 'Кузов: Родстер'
        privod = 'Привод: Задний'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/bmw/z4/1124788244-11fc1245/', parse_mode='html')

        name2 = 'BMW X2 xDrive25i, 2024'
        color2 = 'Цвет: Синий'
        cash2 = '7.699.900 ₽'
        year2 = 'Год выпуска: 2024'
        probeg2 = 'Пробег: 20 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 204 л.с./ 2.0 л / Бензин'
        kuzov2 = 'Кузов: Внедорожник 5 дв.'
        privod2 = 'Привод: Полный'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/bmw/x2/1125228996-c5bf0da5/',parse_mode='html')

        name3 = 'BMW X3 M Competition, 2021'
        color3 = 'Цвет: Белый'
        cash3 = '9.025.000 ₽'
        year3 = 'Год выпуска: 2021'
        probeg3 = 'Пробег: 40.000 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 510 л.с./ 3.0 л / Бензин'
        kuzov3 = 'Кузов: Внедорожник 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/bmw/x3_m/1124212561-da041176/',parse_mode='html')



    elif call.data == 'Audi':
        name = 'Audi e-tron 55, 2021'
        color = 'Цвет: Синий'
        cash = '6.983.000 ₽'
        year = 'Год выпуска: 2021'
        probeg = 'Пробег: 10.931 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 408 л.с./ 300 кВт / Электро'
        kuzov = 'Кузов: Внедорожник 5 дв.'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/audi/e_tron/1122479469-0db7f670/', parse_mode='html')

        name2 = 'Audi A6 45 TDI, 2020'
        color2 = 'Цвет: Белый'
        cash2 = '5.990.000 ₽'
        year2 = 'Год выпуска: 2020'
        probeg2 = 'Пробег: 29.001 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 231 л.с./ 3.0л / Дизель'
        kuzov2 = 'Кузов: Седан'
        privod2 = 'Привод: Полный'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/audi/a6/1125146951-d73233ed/',parse_mode='html')

        name3 = 'Audi A6 40 TDI, 2019'
        color3 = 'Цвет: Черный'
        cash3 = '3.354.000 ₽'
        year3 = 'Год выпуска: 2019'
        probeg3 = 'Пробег: 133.000 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 204 л.с. / 2.0 л. / Дизель'
        kuzov3 = 'Кузов: Универсал 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/audi/a6/1124929459-bddf7818/',parse_mode='html')


    elif call.data == 'Mazda':
        name = 'Mazda CX-5, 2024'
        color = 'Цвет: Серый'
        cash = '6.800.000 ₽'
        year = 'Год выпуска: 2024'
        probeg = 'Пробег: Без пробега'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 194 л.с./ 2.5 л. / Бензин'
        kuzov = 'Кузов: Внедорожник 5 дв.'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/new/group/mazda/cx_5/23556288/23556612/1125405813-6214e05e/', parse_mode='html')

        name2 = 'Mazda 6 Atenza, 2023'
        color2 = 'Цвет: Голубой'
        cash2 = '4.290.000 ₽'
        year2 = 'Год выпуска: 2023'
        probeg2 = 'Пробег: Без пробега'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 192 л.с./ 2.5 л. / Бензин'
        kuzov2 = 'Кузов: Седан'
        privod2 = 'Привод: Передний'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/new/group/mazda/6/21419824/23395036/1122993433-05959dbc/',parse_mode='html')

        name3 = 'Mazda 6, 2019'
        color3 = 'Цвет: Белый'
        cash3 = '3.500.000 ₽'
        year3 = 'Год выпуска: 2019'
        probeg3 = 'Пробег: 98.000 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 194 л.с. / 2.5 л. / Бензин'
        kuzov3 = 'Кузов: Седан'
        privod3 = 'Привод: Передний'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/mazda/6/1125490746-b583f752/',parse_mode='html')


    elif call.data == 'Lexus':
        name = 'Lexus LX 450d, 2016'
        color = 'Цвет: Белый'
        cash = '6.599.999 ₽'
        year = 'Год выпуска: 2016'
        probeg = 'Пробег: 189.000 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 272 л.с./ 4.5 л. / Дизель'
        kuzov = 'Кузов: Внедорожник 5 дв.'
        privod = 'Привод: Полный'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/lexus/lx/1124531784-17348801/', parse_mode='html')

        name2 = 'Lexus RX 350, 2024'
        color2 = 'Цвет: Черный'
        cash2 = '11.950.000 ₽'
        year2 = 'Год выпуска: 2024'
        probeg2 = 'Пробег: 20 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 249 л.с./ 2.4 л. / Бензин'
        kuzov2 = 'Кузов: Внедорожник 5 дв.'
        privod2 = 'Привод: Полный'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/lexus/rx/1125413651-c6128d71/',parse_mode='html')

        name3 = 'Lexus RX 500h, 2023'
        color3 = 'Цвет: Черный'
        cash3 = '12.790.000 ₽'
        year3 = 'Год выпуска: 2023'
        probeg3 = 'Пробег: 100 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 371 л.с. / 2.4 л. / Гибрид'
        kuzov3 = 'Кузов: Внедорожник 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/lexus/rx/1124171035-ad6a48a7/',parse_mode='html')

    # ===========

    elif call.data == 'Lada':
        name = 'Lada (ВАЗ) Vesta SW Cross, 2024'
        color = 'Цвет: Белый'
        cash = '2.010.900 ₽'
        year = 'Год выпуска: 2024'
        probeg = 'Пробег: Без пробега'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 122 л.с./ 1.8 л. / Бензин'
        kuzov = 'Кузов: Универсал 5 дв.'
        privod = 'Привод: Передний'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/new/group/vaz/vesta/23900577/24014270/1125344513-a7f021f2/', parse_mode='html')

        name2 = 'Lada (ВАЗ) Granta, 2024'
        color2 = 'Цвет: Серебристый'
        cash2 = '1.067.000 ₽'
        year2 = 'Год выпуска: 2024'
        probeg2 = 'Пробег: Без пробега'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 106 л.с./ 1.6 л. / Бензин'
        kuzov2 = 'Кузов: Седан'
        privod2 = 'Привод: Передний'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/new/group/vaz/granta/21377540/23924470/1125344512-eebda176/',parse_mode='html')

        name3 = 'Lada (ВАЗ) Niva, 2024'
        color3 = 'Цвет: Черный'
        cash3 = '1.403.900 ₽'
        year3 = 'Год выпуска: 2024'
        probeg3 = 'Пробег: Без пробега'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 80 л.с. / 1.7 л. / Бензин'
        kuzov3 = 'Кузов: Внедорожник 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/new/group/vaz/niva/22716614/23805296/1118054807-76f016a1/',parse_mode='html')


    elif call.data == 'Kia':
        name = 'Kia Rio, 2010'
        color = 'Цвет: Черный'
        cash = '315.000 ₽'
        year = 'Год выпуска: 2010'
        probeg = 'Пробег: 313.212 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 95 л.с./ 1.4 л. / Бензин'
        kuzov = 'Кузов: Седан'
        privod = 'Привод: Передний'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/kia/rio/1125142150-fac1aae7/', parse_mode='html')

        name2 = 'Kia Rio X, 2021'
        color2 = 'Цвет: Серебристый'
        cash2 = '1.599.300 ₽'
        year2 = 'Год выпуска: 2021'
        probeg2 = 'Пробег: 65.000 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 100 л.с./ 1.4 л. / Бензин'
        kuzov2 = 'Кузов: Хетчбек 5 дв.'
        privod2 = 'Привод: Передний'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/kia/rio/1124938134-63709c99/',parse_mode='html')

        name3 = 'Kia Rio, 2022'
        color3 = 'Цвет: Черный'
        cash3 = '1.900.000 ₽'
        year3 = 'Год выпуска: 2022'
        probeg3 = 'Пробег: 42.000 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 123 л.с. / 1.6 л. / Бензин'
        kuzov3 = 'Кузов: Седан'
        privod3 = 'Привод: Передний'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/kia/rio/1124263362-02dea3e1/',parse_mode='html')

    elif call.data == 'Datsun':
        name = 'Datsun on-DO, 2020'
        color = 'Цвет: Серый'
        cash = '945.000 ₽'
        year = 'Год выпуска: 2020'
        probeg = 'Пробег: 53.068 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 87 л.с./ 1.6 л. / Бензин'
        kuzov = 'Кузов: Седан'
        privod = 'Привод: Передний'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/datsun/on_do/1123221212-2dbc09dd/', parse_mode='html')

        name2 = 'Datsun mi-DO, 2015'
        color2 = 'Цвет: Голубой'
        cash2 = '600.000 ₽'
        year2 = 'Год выпуска: 2015'
        probeg2 = 'Пробег: 47.000 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 87 л.с./ 1.6 л. / Бензин'
        kuzov2 = 'Кузов: Хетчбек 5 дв.'
        privod2 = 'Привод: Передний'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/datsun/mi_do/1125479919-4c584967/',parse_mode='html')

        name3 = 'Datsun on-DO, 2014'
        color3 = 'Цвет: Черный'
        cash3 = '599.999 ₽'
        year3 = 'Год выпуска: 2014'
        probeg3 = 'Пробег: 75.000 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 87 л.с. / 1.6 л. / Бензин'
        kuzov3 = 'Кузов: Седан'
        privod3 = 'Привод: Передний'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/datsun/on_do/1121412962-5b594c2e/',parse_mode='html')

    elif call.data == 'Dacia':
        name = 'Dacia Duster, 2010'
        color = 'Цвет: Белый'
        cash = '700.000 ₽'
        year = 'Год выпуска: 2010'
        probeg = 'Пробег: 400.000 км'
        have = 'В НАЛИЧИИ'
        engine = 'Двигатель: 90 л.с./ 1.5 л. / Дизель'
        kuzov = 'Кузов: Внедорожник 5 дв.'
        privod = 'Привод: Передний'
        sost = 'Состояние: Не требуется ремонт'
        pts = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name}\n{color}\n\n<b>{cash}\n</b>\n{year}\n{probeg}\n{have}\n{engine}\n{kuzov}\n{privod}\n{sost}\n{pts}\n\n\nhttps://auto.ru/cars/used/sale/dacia/duster/1125576306-25f6eb71/', parse_mode='html')

        name2 = 'Dacia Duster, 2020'
        color2 = 'Цвет: Белый'
        cash2 = '1.400.000 ₽'
        year2 = 'Год выпуска: 2020'
        probeg2 = 'Пробег: 148.000 км'
        have2 = 'В НАЛИЧИИ'
        engine2 = 'Двигатель: 116 л.с./ 1.5 л. / Дизель'
        kuzov2 = 'Кузов: Внедорожник 5 дв.'
        privod2 = 'Привод: Передний'
        sost2 = 'Состояние: Не требуется ремонт'
        pts2 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name2}\n{color2}\n\n<b>{cash2}\n</b>\n{year2}\n{probeg2}\n{have2}\n{engine2}\n{kuzov2}\n{privod2}\n{sost2}\n{pts2}\n\n\nhttps://auto.ru/cars/used/sale/dacia/duster/1125281347-a2486779/',parse_mode='html')

        name3 = 'Dacia Duster, 2018'
        color3 = 'Цвет: Черный'
        cash3 = '1.430.000 ₽'
        year3 = 'Год выпуска: 2018'
        probeg3 = 'Пробег: 93.000 км'
        have3 = 'В НАЛИЧИИ'
        engine3 = 'Двигатель: 125 л.с. / 1.2 л. / Бензин, газобалонное оборудование'
        kuzov3 = 'Кузов: Внедорожник 5 дв.'
        privod3 = 'Привод: Полный'
        sost3 = 'Состояние: Не требуется ремонт'
        pts3 = 'ПТС: Оригинал'
        bot.send_message(call.message.chat.id,f'{name3}\n{color3}\n\n<b>{cash3}\n</b>\n{year3}\n{probeg3}\n{have3}\n{engine3}\n{kuzov3}\n{privod3}\n{sost3}\n{pts3}\n\n\nhttps://auto.ru/cars/used/sale/dacia/duster/1124704550-645dc14b/',parse_mode='html')



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