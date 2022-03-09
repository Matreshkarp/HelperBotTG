import telebot
from telebot import types

token='5134848374:AAHeMp3VJIw8nLXcreBYRBZ9L7uxI17-KCw'

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
 keyboard=types.ReplyKeyboardMarkup(True)
 calcu=types.KeyboardButton('💉Рандомайзер')
 info=types.KeyboardButton('ℹ️Информация о боте')
 buttons_to_add=[calcu, info]


 keyboard.add(*buttons_to_add)
   
 bot.send_message(message.chat.id, "Привет!Выбери то что тебе надо и используй с удовольствием.", reply_markup=keyboard)
    
# if text == 'ℹ️Информация о боте'
 #bot.send_message(message.chat.id, 'f')

bot.polling(none_stop=True)