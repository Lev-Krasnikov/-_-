import telebot

bot = telebot.TeleBot("5955212342:AAG8Oorj41wOnxWF0NPqqIOlWZz4ufN5RBY")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет')

@bot.message_handler(commands=['поговорим?'])
def start(message):
    mess_2 = f'О чем хочешь поговорить, <b>{message.from_user.first_name}</b>?'
    bot.send_message(message.chat.id, mess_2, parse_mode='html')

@bot.message_handler(commands=['как_дела?'])
def start(message):
    mess_3 = f'отлично, спасибо, как ты, <b>{message.from_user.first_name}</b>?'
    bot.send_message(message.chat.id, mess_3, parse_mode='html')

@bot.message_handler(commands=['чем_занимаешься?'])
def start(message):
    mess_4 = f'разрабатываю чат бота'
    bot.send_message(message.chat.id, mess_4, parse_mode='html')

@bot.message_handler(commands=['help'])
def start(message):
    mess = f'Чем могу помочь, {message.from_user.first_name} ?'

@bot.message_handler(content_types=['photo'])
def get_user_photo (message):
    bot.send_message(message.chat.id, 'вау, крутое фото!')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id }", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "я тебя не понимаю")



@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("посетить веб сайт",  url="https://www.google.ru/?hl="))
    bot.send_message(message.chat.id, 'перейдите на сайт!', reply_markup=markup)


bot.polling(none_stop=True)