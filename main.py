import telebot
import json

from self import self
from telebot import types
import sqlite3
import buttons
import db
import config
import inlineLocation
from keyBoard import KeyBoard

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])  # спрацьовує при команді "\start"
def start(message):
    KeyBoard.start(message)


@bot.message_handler()  # спрацьовує при отриманні будь якого повідомлення
def bot_message(message):
    if message.text == 'Моя Карта':
        buttons.my_card(message)
    elif message.text == 'Показати контакт':
        db.send_qr(message)
    elif message.text == 'Повернутися':
        buttons.start(message)
    elif message.text == 'Наші магазини':
        KeyBoard.town_location(message)


@bot.message_handler(content_types=['contact'])
def connect(message):  # спрацьовує, коли отримує контакт користовуча
    db.append_user(message)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    location = KeyBoard()
    lon = 24.2399975153407
    lat = 50.3982047230818
    if call.data == 'CHERVONOGRAD':
        location.chervonograd_location(call)

    elif call.data == 'NOVOVOLINSK':
        location.novovolynsk_location(call)
    elif call.data == 'ZHOVKVA':
        bot.send_location(call.message.chat.id, longitude=lon, latitude=lat)
    elif call.data == 'VOLODYMYR':
        location.volodumyr_location(call)
    elif call.data == 'SOKAL':
        location.sokal_location(call)
    elif call.data == 'SOSNIVKA':
        bot.send_location(call.message.chat.id, longitude=lon, latitude=lat)
    elif call.data == 'DOBROTVIR':
        bot.send_location(call.message.chat.id, longitude=lon, latitude=lat)
    elif call.data == 'HOROKHIV':
        bot.send_location(call.message.chat.id, longitude=lon, latitude=lat)


bot.polling(none_stop=True)
