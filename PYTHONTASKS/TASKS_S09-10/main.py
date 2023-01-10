import telebot
from config import TOKEN
import requests
import json


bot = telebot.TeleBot(TOKEN)


HELP = """
/help - вывести список доступных команд
/calc - выполнить расчет (сложение, вычетание, умножение, деление - одно действие в строку)
/print - напечатать все расчеты
/exit - завершение программы"""


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
    item_joke = telebot.types.KeyboardButton('Joke')
    item_help = telebot.types.KeyboardButton('Help')

    markup.add(item_joke, item_help)
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


key_words = "Boss"


@bot.message_handler(content_types=["text"])
def echo(message):
    if key_words in message.text:
        bot.send_message(message.chat.id, "Greet you my master!")
    # elif message.text == 'Calc':
    #     bot.send_message(message.chat.id, 'Sorry, feature under development')
    elif message.text == 'Joke':
        # chuck_url = requests.get('https://api.chucknorris.io/jokes/random')
        # bot.send_message(message.chat.id, json.dumps(chuck_url.json(), indent=2))
        bot.send_message(message.chat.id, get_joke())
    elif message.text == 'Help':
        help_menu(message)
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
