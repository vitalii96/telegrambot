import telebot
from telebot import types
import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(config.TOKEN)


def start(message):
    mess = f'Привіт, {message.from_user.first_name}{message.from_user.last_name}'
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # створюєм екземпляр класу кнопок на клаві та вказуємо, що вони міняють розмір відповідно до кількості
    item1 = types.KeyboardButton('Моя Карта')
    item2 = types.KeyboardButton('Наші магазини')
    item3 = types.KeyboardButton('Гаманець')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, mess, reply_markup=markup)


def my_card(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Відправити свій контакт',
                                 request_contact=True)  # при натисненні відправляє контакт
    item2 = types.KeyboardButton('Показати контакт')
    item3 = types.KeyboardButton('Повернутися')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Меню карти', reply_markup=markup)
