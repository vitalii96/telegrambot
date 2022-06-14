import telebot
from telebot import types
import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(config.TOKEN)


def town_location(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    link1 = types.InlineKeyboardButton(text='Червоноград', callback_data='CHERVONOGRAD')
    link2 = types.InlineKeyboardButton(text='Нововолинськ', callback_data='NOVOVOLINSK')
    link3 = types.InlineKeyboardButton(text='Володимир', callback_data='VOLODYMYR')
    link4 = types.InlineKeyboardButton(text='Сокаль', callback_data='SOKAL')
    link5 = types.InlineKeyboardButton(text='Соснівка', callback_data='SOSNIVKA')
    link6 = types.InlineKeyboardButton(text='Добротвір', callback_data='DOBROTVIR')
    link7 = types.InlineKeyboardButton(text='Горохів', callback_data='HOROKHIV')
    link8 = types.InlineKeyboardButton(text='Жовква', callback_data='ZHOVKVA')
    markup.add(link1, link2, link3, link4, link5, link6, link7, link8)
    bot.send_message(chat_id, 'Оберіть місто :', reply_markup=markup)


def sokal_location(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    link1 = types.InlineKeyboardButton(text='Шептицького,59', callback_data='SHEPT')
    link2 = types.InlineKeyboardButton(text='Героїв УПА', callback_data='UPA')
    markup.add(link1, link2)
    bot.send_message(chat_id, 'Наші магазини в місті Сокаль :', reply_markup=markup)


def chervonograd_location(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    link1 = types.InlineKeyboardButton(text='Стуса,17', callback_data='STUSA')
    link2 = types.InlineKeyboardButton(text='Бандери,11', callback_data='BANDERY')
    link3 = types.InlineKeyboardButton(text='Шевченка,23', callback_data='SHEV23')
    link4 = types.InlineKeyboardButton(text='Шевченка,14', callback_data='SHEV14')
    link5 = types.InlineKeyboardButton(text='Бандери,20', callback_data='MAFBANDERY')
    link6 = types.InlineKeyboardButton(text='Кутова,20', callback_data='KUTOVA')
    markup.add(link1, link2, link3, link4, link5, link6)
    bot.send_message(chat_id, 'Наші магазини в місті Червоноград :', reply_markup=markup)


def novovolynsk_location(message):
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup()
    link1 = types.InlineKeyboardButton(text='Шахтарська,1', callback_data='SHAHT')
    link2 = types.InlineKeyboardButton(text='Нововолинська,57', callback_data='AMIGO')
    link3 = types.InlineKeyboardButton(text='15 мікрорайон', callback_data='KAKTUS')
    markup.add(link1, link2, link3)
    bot.send_message(chat_id, 'Наші магазини в місті Сокаль :', reply_markup=markup)
