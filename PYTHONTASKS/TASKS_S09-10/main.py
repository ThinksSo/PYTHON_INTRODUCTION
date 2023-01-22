import telebot
import wikipedia, re

# from xmlrpc.client import DateTime
# from telethon.sync import TelegramClient

# from telethon.tl.functions.messages import GetDialogsRequest
# from telethon.tl.types import InputPeerEmpty
# from telethon.tl.functions.messages import GetHistoryRequest
# from telethon.tl.types import PeerChannel


from config import TOKEN
from config import phone
from config import api_id
from config import api_hash

import requests
import json
import csv


bot = telebot.TeleBot(TOKEN)


HELP = """
/help - вывести список доступных команд
/wiki - поиск в Википедии
/calc - выполнить расчет (сложение, вычетание, умножение, деление - одно действие в строку)
/weather - прогноз погоды в выбранном городе
/print - напечатать все расчеты
/exit - завершение программы"""


# client = TelegramClient(phone, api_id, api_hash)
# client.start()


def get_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = json.loads(response.text)
    return(joke['value'])


"""START"""


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hi! You are welcome')
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item_calc = telebot.types.KeyboardButton('Calc')
    # item_weather = telebot.types.KeyboardButton('Joke')
    item_joke = telebot.types.KeyboardButton('Joke')
    item_wiki = telebot.types.KeyboardButton('Wiki')
    item_help = telebot.types.KeyboardButton('Help')

    markup.add(item_joke, item_wiki)
    markup.add(item_help)
    bot.send_message(
        message.chat.id, 'Click the button below the text entry', reply_markup=markup)


@bot.message_handler(commands=["help"])
def help_menu(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["print"])
def show(message):
    bot.send_message(message.chat.id, 'Sorry, feature under development')


@bot.message_handler(commands=["calc"])
def show(message):
    bot.send_message(message.chat.id, 'Sorry, feature under development')


@bot.message_handler(commands=["wiki"])
def wiki(message):
    bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
    bot.register_next_step_handler(message, handle_text)


def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


key_words = "Boss"


@bot.message_handler(content_types=["text"])
def echo(message):
    if key_words in message.text:
        bot.send_message(message.chat.id, "Greet you my master!")
    # elif message.text == 'Calc':
    #     bot.send_message(message.chat.id, 'Sorry, feature under development')
    elif message.text == 'Joke':
        bot.send_message(message.chat.id, get_joke())
    elif message.text == 'Help':
        help_menu(message)
    elif message.text == 'Wiki' or message.text == 'wiki':
        wiki(message)
    else:
        bot.send_message(message.chat.id, message.text)


wikipedia.set_lang("ru")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


bot.polling(none_stop=True)
