import telebot

import platform

import subprocess

import time

bot = telebot.TeleBot('')
storage = {}
def init_storage(user_id):

    storage[user_id] = dict(host=None)

def store_number(user_id, key, value):

    storage[user_id][key] = dict(value=value)

def get_number(user_id, key):

    return storage[user_id][key].get('value')

@bot.message_handler(commands=['start'])#початок
def strn(message):

    bot.send_message(message.chat.id, f'<b> Привіт <i>{message.from_user.first_name} {message.from_user.last_name}</i> </b>',  parse_mode = 'html')
    time.sleep(1)
    init_storage(message.from_user.id)
    bot.reply_to(message, "Ваш  хост нейм?")
    bot.register_next_step_handler(message,adress)


def adress(message):
    host = message.text
    store_number(message.from_user.id, "host", host)
    ip = get_number(message.from_user.id, "host")
    time.sleep(1)

    bot.send_message(message.chat.id, f"За цим хост неймом буде перевірятися світло:  {ip}" ,  parse_mode = 'html')

    def ping(ip):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', ip]
        return subprocess.call(command) == 0
    


    status = 0
    while True:#цикл з'ясування наявносі світла
        kif = ping(ip)

        if kif == True and status == 1:
            bot.send_message(message.chat.id,"У вас з'вилося світло")
            status = 0
        if kif == False and status == 0:
            bot.send_message(message.chat.id,'У вас зникло світло')
            status = 1

        time.sleep(100)
if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling(none_stop=True)
