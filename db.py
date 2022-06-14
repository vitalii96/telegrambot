import sqlite3
import telebot
import json
from telebot import types
import buttons
import db


bot = telebot.TeleBot('5364648448:AAFpMywijzTgH85o7xJoOaUPJJWDGBh1Pxc')

connect = sqlite3.connect('users.db', check_same_thread=False)
cursor = connect.cursor()
# cursor.execute(
#     """CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER,
#         name STRING,
#         last_name STRING,
#         phone_number STRING)""")
# connect.commit()


def append_user(message):
    if message.contact is not None:  # якщо об'єкт "contact" не порожній
        user_phone = message.contact.phone_number
        user_id = message.chat.id
        user_name = message.from_user.first_name
        user_lastName = message.from_user.last_name

        print(user_phone)  # виводиться в консоль номер телефону

        cursor.execute(f"SELECT user_id FROM users WHERE user_id={user_id}")
        data = cursor.fetchone()
        if data is None:
            user_info = [user_id, user_name, user_lastName, user_phone]
            cursor.execute("""INSERT INTO users VALUES(?,?,?,?);""", user_info)
            connect.commit()
        else:
            bot.send_message(message.chat.id, 'Такий користувач вже існує')


def send_qr(message):
    user_id = message.chat.id
    cursor.execute(f"SELECT qr_code FROM users WHERE user_id={user_id}")
    qr_code = cursor.fetchall()
    l = []
    for row in qr_code :
        for x in row:
            l.append(x)
    print(l[0])


    send_photo = open(l[0], 'rb')
    bot.send_photo(user_id, send_photo)
