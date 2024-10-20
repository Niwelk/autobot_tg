import telebot
from telebot import types
bot = telebot.TeleBot("7401092703:AAEUIl1C1Q7UGDuV6C90OUyNrDuzhfks16I")

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
    kbd.add(marka1,marka2,marka3,marka4)
    return kbd
def inline2m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Volkswagen", callback_data='Volkswagen')
    marka2 = types.InlineKeyboardButton("BMW", callback_data='BMW')
    marka3 = types.InlineKeyboardButton("Cadillac", callback_data='Cadillac')
    marka4 = types.InlineKeyboardButton("Lexus", callback_data='Lexus')
    marka5 = types.InlineKeyboardButton("Jaguar", callback_data='Jaguar')
    kbd.add(marka1,marka2,marka3,marka4, marka5)
    return kbd
def inline3m():
    kbd = types.InlineKeyboardMarkup(row_width=1)
    marka1 = types.InlineKeyboardButton("Rolls-Royce", callback_data='Rolls-Royce')
    marka2 = types.InlineKeyboardButton("Bentley", callback_data='Bentley')
    marka3 = types.InlineKeyboardButton("Bugatti", callback_data='Bugatti')
    marka4 = types.InlineKeyboardButton("Paganini", callback_data='Paganini')
    kbd.add(marka1,marka2,marka3,marka4)
    return kbd

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b>! Выбери категорию автомобиля",parse_mode='html', reply_markup=inline1())

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