import telebot
from telebot import types
import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(config.TOKEN)


class KeyBoard:

    def start(self):
        mess = f'Привіт, {self.from_user.first_name}{self.from_user.last_name}'
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True)  # створюєм екземпляр класу кнопок на клаві та вказуємо, що вони міняють розмір відповідно до кількості
        item1 = types.KeyboardButton('Моя Карта')
        item2 = types.KeyboardButton('Наші магазини')
        item3 = types.KeyboardButton('Гаманець')
        markup.add(item1, item2, item3)
        bot.send_message(self.chat.id, mess, reply_markup=markup)

    def chervonograd_location(self, call):
        markup = types.InlineKeyboardMarkup()
        link1 = types.InlineKeyboardButton(text='Стуса,17', callback_data='STUSA')
        link2 = types.InlineKeyboardButton(text='Бандери,11', callback_data='BANDERY')
        link3 = types.InlineKeyboardButton(text='Шевченка,23', callback_data='SHEV23')
        link4 = types.InlineKeyboardButton(text='Шевченка,14', callback_data='SHEV14')
        link5 = types.InlineKeyboardButton(text='Бандери,20', callback_data='MAFBANDERY')
        link6 = types.InlineKeyboardButton(text='Кутова,20', callback_data='KUTOVA')
        markup.add(link1, link2, link3, link4, link5, link6)
        bot.send_message(call.from_user.id, 'Наші магазини в місті Червоноград :', reply_markup=markup)

    def town_location(self):
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
        bot.send_message(self.from_user.id, 'Оберіть місто :', reply_markup=markup)

    def sokal_location(self, call):
        markup = types.InlineKeyboardMarkup()
        link1 = types.InlineKeyboardButton(text='Шептицького,59', callback_data='SHEPT')
        link2 = types.InlineKeyboardButton(text='Героїв УПА', callback_data='UPA')
        markup.add(link1, link2)
        bot.send_message(call.from_user.id, 'Наші магазини в місті Сокаль :', reply_markup=markup)

    def novovolynsk_location(self, call):
        chat_id = call.from_user.id
        markup = types.InlineKeyboardMarkup()
        link1 = types.InlineKeyboardButton(text='Шахтарська,1', callback_data='SHAHT')
        link2 = types.InlineKeyboardButton(text='Нововолинська,57', callback_data='AMIGO')
        link3 = types.InlineKeyboardButton(text='15 мікрорайон', callback_data='KAKTUS')
        markup.add(link1, link2, link3)
        bot.send_message(chat_id, 'Наші магазини в місті Сокаль :', reply_markup=markup)
    def volodumyr_location(self, call):
        chat_id = call.from_user.id
        markup = types.InlineKeyboardMarkup()
        link1 = types.InlineKeyboardButton(text='Ковельська,99', callback_data='OPTYKA')
        link2 = types.InlineKeyboardButton(text='Ковельська,100', callback_data='RK')
        markup.add(link1, link2)
        bot.send_message(chat_id, 'Наші магазини в місті Сокаль :', reply_markup=markup)