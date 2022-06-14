import telebot
from telebot import types
import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(config.TOKEN)


class KeyBoard():
    age = 10
    def start(self):
        mess = f'Привіт, {self.from_user.first_name}{self.from_user.last_name}'
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True)  # створюєм екземпляр класу кнопок на клаві та вказуємо, що вони міняють розмір відповідно до кількості
        item1 = types.KeyboardButton('Моя Карта')
        item2 = types.KeyboardButton('Наші магазини')
        item3 = types.KeyboardButton('Гаманець')
        markup.add(item1, item2, item3)
        bot.send_message(self.chat.id, mess, reply_markup=markup)

    def chervonograd_location(self):
        chat_id = self.chat.id
        markup = types.InlineKeyboardMarkup()
        link1 = types.InlineKeyboardButton(text='Стуса,17', callback_data='STUSA')
        link2 = types.InlineKeyboardButton(text='Бандери,11', callback_data='BANDERY')
        link3 = types.InlineKeyboardButton(text='Шевченка,23', callback_data='SHEV23')
        link4 = types.InlineKeyboardButton(text='Шевченка,14', callback_data='SHEV14')
        link5 = types.InlineKeyboardButton(text='Бандери,20', callback_data='MAFBANDERY')
        link6 = types.InlineKeyboardButton(text='Кутова,20', callback_data='KUTOVA')
        markup.add(link1, link2, link3, link4, link5, link6)
        bot.send_message(chat_id, 'Наші магазини в місті Червоноград :', reply_markup=markup)