import telebot
import random
import wikipedia as wkp
 
from telebot import types
 
bot = telebot.TeleBot("1191699863:AAGisx_Riems732iRr-2eDbdiNbaA0sMZ54")
 
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, "Здравствуйте, {0.first_name}!\nЯ - <b>{1.first_name}</b>, заказывайте вкуснейшую пиццу по командам.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['order'])
def handle_text (message):
    bot.send_message(message.chat.id, "Выберите тип пиццы по командам с помощью /")

@bot.message_handler(commands=['margarita'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Маргарита. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['vetchina_griby'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Ветчина и грибы. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['hawaii'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Гавайская. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['nautical'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Морская. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['mushroom'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Грибная. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['vegetarian'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Вегетарианская. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['meat'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Мясная. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['sweet'])
def handle_text (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("30 см", callback_data='small')
    item2 = types.InlineKeyboardButton("35 см", callback_data='middle')
    item3 = types.InlineKeyboardButton("40 см", callback_data='big')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выбрана пицца Сладкая. Выберите размер:", reply_markup=markup)

@bot.message_handler(commands=['address'])
def handle_text (message):
    bot.send_message(message.chat.id, "Напишите адреc.")
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        txt = message.text
        bot.send_message(message.chat.id, "Ваша пицца будет доставлена по адресу: {0}. Ожидайте курьера.".format(txt))

 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'small':
                bot.send_message(call.message.chat.id, 'Выбран размер 30см. Теперь напишите адрес, выбрав команду /address.')
            elif call.data == 'middle':
                bot.send_message(call.message.chat.id, 'Выбран размер 35см. Теперь напишите адрес, выбрав команду /address.')
            elif call.data == 'big':
                bot.send_message(call.message.chat.id, 'Выбран размер 40см. Теперь напишите адрес, выбрав команду /address.')
 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = ':)',
                reply_markup=None)
 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Очистил.")
 
    except Exception as e:
        print(repr(e))
        
bot.polling(none_stop=True)
