import telebot
import json

bot = telebot.TeleBot('5364648448:AAFpMywijzTgH85o7xJoOaUPJJWDGBh1Pxc')
user_list = []


def user_text(message):
    user_list.append(message.text)  # додаю в список повідомлення юзера
    user_message = ' '.join(user_list)
    with open('user_text.json', 'a') as file:
        json.dump(user_message, file)
    bot.send_message(message.chat.id, user_message)  # вивожу строку
