import random
import telebot
from telebot import types

token ="Youre token"
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('вычислить')
itembtn2 = types.KeyboardButton('играть')

markup.add(itembtn1, itembtn2)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "Привет, тебя приветсвует бот помощник",reply_markup=markup)

@bot.message_handler(content_types=['text'])
def recod_text_commands(message):
    global game_started
    global r_number
    data = open('messages.txt', 'a', encoding='utf-8')
    text = f'{message.from_user.first_name} {message.from_user.last_name} {message.from_user.id}: {message.text}'
    data.writelines(f'{text}\n')
    # bot.reply_to(message, message.text)
    if game_started:
        if message.text.isdigit():
            number = int(message.text)
            if number > r_number:
                bot.reply_to(message, 'Число которое я загадал меньше')
            elif number < r_number:
                bot.reply_to(message, 'Число которое я загадал больше')    
            elif number == r_number:
                bot.reply_to(message, 'Поздравляю!!! Ты угадал число!')    
            else:
              bot.reply_to(message, 'Ничего не понял')  
        else:
            bot.reply_to(message, 'Я ожидал число...')
        # return
    

    elif message.text == 'играть':
        if not game_started:
            game_started = True
            r_number = random.randint(1,1000)
            bot.reply_to(message, 'Я задумал число от 1 до 1000 Попробуй отгадать')  
        else:
            bot.reply_to(message, 'игра уже идет')

    elif message.text == 'вычислить':
        bot.reply_to(message, 'введи выражение')
        bot.register_next_step_handler(message, calculater)

def calculater(message):
    try:
        bot.reply_to(message, f'ответ: {eval(message.text)}')     
    except NameError:
        bot.reply_to(message, 'вы ввели неверное выражние')

bot.infinity_polling()

