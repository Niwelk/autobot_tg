import telebot
from telebot import types
bot = telebot.TeleBot('7401092703:AAEUIl1C1Q7UGDuV6C90OUyNrDuzhfks16I')

def inline1():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    class1 = types.InlineKeyboardButton("Бюджет", callback_data='Бюджет')
    class2 = types.InlineKeyboardButton("Премиум", callback_data='Премиум')
    class3 = types.InlineKeyboardButton("Люкс", callback_data='Люкс')
    kbd.add(class1,class2,class3)
    return kbd

def inline1m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Dacia", callback_data='Dacia')
    marka2 = types.InlineKeyboardButton("Datsun", callback_data='Datsun')
    marka3 = types.InlineKeyboardButton("Lada", callback_data='Lada')
    marka4 = types.InlineKeyboardButton("Kia", callback_data='Kia')
    back = types.InlineKeyboardButton("(назад)", callback_data='(назад)')
    kbd.add(marka1,marka2,marka3,marka4, back)
    return kbd

def inline2m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Volkswagen", callback_data='Volkswagen')
    marka2 = types.InlineKeyboardButton("BMW", callback_data='BMW')
    marka3 = types.InlineKeyboardButton("Cadillac", callback_data='Cadillac')
    marka4 = types.InlineKeyboardButton("Lexus", callback_data='Lexus')
    marka5 = types.InlineKeyboardButton("Jaguar", callback_data='Jaguar')
    back = types.InlineKeyboardButton("(назад)", callback_data='(назад)')
    kbd.add(marka1,marka2,marka3,marka4, marka5, back)
    return kbd

def inline3m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Rolls-Royce", callback_data='Rolls-Royce')
    marka2 = types.InlineKeyboardButton("Bentley", callback_data='Bentley')
    marka3 = types.InlineKeyboardButton("Bugatti", callback_data='Bugatti')
    marka4 = types.InlineKeyboardButton("Paganini", callback_data='Paganini')
    back = types.InlineKeyboardButton("(назад)", callback_data='(назад)')
    kbd.add(marka1,marka2,marka3,marka4, back)
    return kbd

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'Бюджет' or call.data == 'Премиум' or call.data == 'Люкс':
        bot.send_message(call.message.chat.id, "Вы выбрали " + call.data, reply_markup=inline1m())
    elif call.data in ['Dacia', 'Datsun', 'Lada', 'Kia']:
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