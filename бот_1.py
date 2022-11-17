
import telebot




from pythonping import ping
import time


bot = telebot.TeleBot('5752748301:AAFxZprMFki5pr7Tw1AUgx6gsHNjLQkSYjA')
response_list = ping('tststsfam.tplinkdns.com')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<b> Привіт <i>{message.from_user.first_name} {message.from_user.last_name}</i> </b>', parse_mode='html')
@bot.message_handler(commands=['info'])
def start(message):
    bot.send_message(message.chat.id, f'<b> Привіт <i>{message.from_user.first_name} {message.from_user.last_name}</i> Я можу сказати чи є в тебе зараз світло вдома чи ні </b>', parse_mode='html')
@bot.message_handler(commands=['light'])
def start(message):
    #bot.send_message(message.chat.id,response_list.rtt_avg_ms)
    bot.send_message(message.chat.id,'👀Перевіряю...')
    time.sleep(1.5)

    if response_list.rtt_avg_ms ==0:
        bot.send_message(message.chat.id,f'<b>  <i>{message.from_user.first_name} {message.from_user.last_name}</i> 😟Вам не повезло у вас немає світла 😟</b>',parse_mode='html')
    else:
        bot.send_message(message.chat.id,f'<b>  <i>{message.from_user.first_name} {message.from_user.last_name}</i> ☺Вам повезло у вас є світло ☺</b>',parse_mode='html')

def start(message):
    time.sleep(300)
    if response_list.rtt_avg_ms == 0:
        bot.send_message(message.chat.id,f'<b>  <i>{message.from_user.first_name} {message.from_user.last_name}</i> 😟Вам не повезло у вас немає світла 😟</b>',parse_mode='html')
@bot.message_handler()
def start(message):
    bot.send_message(message.chat.id, f'<b> <i>{message.from_user.first_name} {message.from_user.last_name}</i> Я розумію тіки команди. Ось вони →</b> /info інформація про мене.  /start Ви запускаєте мене  /light перевірка чи є у вас світло', parse_mode='html')


    #if response_list  == 0:
        #bot.send_message(message.chat.id('Світло немає'))
   # if response_list != 0:
       # bot.send_message(message.chat.id('Світло є'))



bot.polling(none_stop=True)