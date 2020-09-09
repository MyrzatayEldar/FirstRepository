import telebot
import random
 
from telebot import types
 
bot = telebot.TeleBot("1196481600:AAHBhH5odNTFraXmlDNtvvYgeY8pFnWQpwg")
 
@bot.message_handler(commands=['start'])
def welcome(message):
    
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("Сколько тебе лет?")
    markup.add(item1, item2, item3)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Как дела?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        elif message.text =='Сколько тебе лет?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("18-40", callback_data='young')
            item2 = types.InlineKeyboardButton("40-70", callback_data='starik')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'Я родился недавно. Младенец. А тебе?', reply_markup=markup)
        elif message.text == 'Какое число тебе нравится?':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("0-100", callback_data='hundred')
            item2 = types.InlineKeyboardButton("100-999", callback_data='nine')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Мне нравится число 5. А тебе? Выбери интервал', reply_markup=markup)
        elif message.text == 'анкетирование':
            bot.send_message(message.chat.id, 'Начинаем анкетирование!')
            bot.send_message(message.chat.id, 'Как вас зовут?')
            bot.send_message(message.chat.id, 'Сколько вам лет?')
            bot.send_message(message.chat.id, 'Откуда вы?')
            bot.send_message(message.chat.id, 'Как ваша фамилия?')
            bot.send_message(message.chat.id, 'Как дела?')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            elif call.data == 'young':
                bot.send_message(call.message.chat.id, 'А вы молодой)')
            elif call.data == 'starik':
                bot.send_message(call.message.chat.id, 'Я слышал, что с возрастом люди красивеют.')
            elif call.data == 'hundred':
                bot.send_message(call.message.chat.id, 'Мое любимое число тоже в этом интервале. Красава!')
            elif call.data == 'nine':
                bot.send_message(call.message.chat.id, 'Любитель трехзначных чисел,Красава!')
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Deleted")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
