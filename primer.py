import telebot
from telebot import types # кнопки
from string import Template

bot = telebot.TeleBot("1191699863:AAGisx_Riems732iRr-2eDbdiNbaA0sMZ54")

user_dict = {}

class User:
    def __init__(self, city):
        self.city = city

        keys = ['fullname', 'phone', 'driverSeria', 
                'driverNumber', 'driverDate', 'car', 
                'carModel', 'carColor', 'carNumber', 'carDate']
        
        for key in keys:
            self.key = None

# если /help, /start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/reg')
    itembtn3 = types.KeyboardButton('/reg2')
    markup.add(itembtn1, itembtn2, itembtn3)
    
    bot.send_message(message.chat.id, "Здравствуйте "
    + message.from_user.first_name
    + ", я бот, чтобы вы хотели узнать?", reply_markup=markup)

# /about
@bot.message_handler(commands=['about'])
def send_about(message):
	bot.send_message(message.chat.id, "Мы надежная компания" 
    + " company. 10 лет на рынке.")

# /reg
@bot.message_handler(commands=["reg"])
def user_reg(message):
       markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
       itembtn1 = types.KeyboardButton('Киев')
       itembtn2 = types.KeyboardButton('Одесса')
       itembtn3 = types.KeyboardButton('Харьков')
       itembtn4 = types.KeyboardButton('Днепр')
       itembtn5 = types.KeyboardButton('Запорожье')
       itembtn6 = types.KeyboardButton('Львов')
       markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

       msg = bot.send_message(message.chat.id, 'Ваш город?', reply_markup=markup)
       bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    try:
        chat_id = message.chat.id
        user_dict[chat_id] = User(message.text)

        # удалить старую клавиатуру
        markup = types.ReplyKeyboardRemove(selective=False)

        msg = bot.send_message(chat_id, 'Фамилия Имя Отчество', reply_markup=markup)
        bot.register_next_step_handler(msg, process_fullname_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_fullname_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.fullname = message.text

        msg = bot.send_message(chat_id, 'Ваш номер телефона')
        bot.register_next_step_handler(msg, process_phone_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_phone_step(message):
    try:
        int(message.text)

        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.phone = message.text

        msg = bot.send_message(chat_id, 'Серия водительского удостоверения')
        bot.register_next_step_handler(msg, process_driverSeria_step)

    except Exception as e:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона.')
        bot.register_next_step_handler(msg, process_phone_step)

def process_driverSeria_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverSeria = message.text

        msg = bot.send_message(chat_id, 'Номер водительского удостоверения')
        bot.register_next_step_handler(msg, process_driverNumber_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_driverNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverNumber = message.text
       
        msg = bot.send_message(chat_id, 'Дата выдачи водительского удостоверения\nВ формате: День.Месяц.Год')
        bot.register_next_step_handler(msg, process_driverDate_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_driverDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.driverDate = message.text

        msg = bot.send_message(chat_id, 'Марка автомобиля')
        bot.register_next_step_handler(msg, process_car_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_car_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.car = message.text

        msg = bot.send_message(chat_id, 'Модель автомобиля')
        bot.register_next_step_handler(msg, process_carModel_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_carModel_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carModel = message.text

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Бежевый')
        itembtn2 = types.KeyboardButton('Белый')
        itembtn3 = types.KeyboardButton('Голубой')
        itembtn4 = types.KeyboardButton('Желтый')
        itembtn5 = types.KeyboardButton('Зеленый')
        itembtn6 = types.KeyboardButton('Коричневый')
        itembtn7 = types.KeyboardButton('Красный')
        itembtn8 = types.KeyboardButton('Оранжевый')
        itembtn9 = types.KeyboardButton('Розовый')
        itembtn10 = types.KeyboardButton('Серый')
        itembtn11 = types.KeyboardButton('Синий')
        itembtn12 = types.KeyboardButton('Фиолетовый')
        itembtn13 = types.KeyboardButton('Черный')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13)

        msg = bot.send_message(chat_id, 'Цвет автомобиля', reply_markup=markup)
        bot.register_next_step_handler(msg, process_carColor_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_carColor_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carColor = message.text

        msg = bot.send_message(chat_id, 'Гос. номер автомобиля')
        bot.register_next_step_handler(msg, process_carNumber_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_carNumber_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carNumber = message.text

        msg = bot.send_message(chat_id, 'Год выпуска')
        bot.register_next_step_handler(msg, process_carDate_step)

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

def process_carDate_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        user.carDate = message.text

        # ваша заявка "Имя пользователя"
        bot.send_message(chat_id, getRegData(user, 'Ваша заявка', message.from_user.first_name), parse_mode="Markdown")
        # отправить в группу
        bot.send_message(config.chat_id, getRegData(user, 'Заявка от бота', bot.get_me().username), parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, 'ooops!!')

# формирует вид заявки регистрации
# нельзя делать перенос строки Template
# в send_message должно стоять parse_mode="Markdown"
def getRegData(user, title, name):
    t = Template('$title *$name* \n Город: *$userCity* \n ФИО: *$fullname* \n Телефон: *$phone* \n Серия водительского удостоверения: *$driverSeria* \n Номер водительского удостоверения: *$driverNumber* \n Дата выдачи водительского удостоверения: *$driverDate* \n Марка автомобиля: *$car* \n Модель автомобиля: *$carModel* \n Цвет автомобиля: *$carColor* \n Гос. номер автомобиля: *$carNumber* \n Год выпуска: *$carDate*')

    return t.substitute({
        'title': title,
        'name': name,
        'userCity': user.city,
        'fullname': user.fullname,
        'phone': user.phone,
        'driverSeria': user.driverSeria,
        'driverNumber': user.driverNumber,
        'driverDate': user.driverDate,
        'car': user.car,
        'carModel': user.carModel,
        'carColor': user.carColor,
        'carNumber': user.carNumber,
        'carDate': user.carDate,
    })

# произвольный текст
@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(message.chat.id, 'О нас - /about\nРегистрация - /reg\nПомощь - /help')

# произвольное фото
@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)
