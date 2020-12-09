from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton("1 😞")
button2 = KeyboardButton("2 😔")
button3 = KeyboardButton("3 😐")
button4 = KeyboardButton("4 🙂")
button5 = KeyboardButton("5 😁")

button6 = KeyboardButton("Да")
button7 = KeyboardButton("Нет")

button8 = KeyboardButton("Совет от бота")
button9 = KeyboardButton("Я знаю, что буду делать")
button10 = KeyboardButton("Спасибо!")
button11 = KeyboardButton("Договорились!")

markup1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3).add(button4).add(button5)
markup2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button6).add(button7)
markup3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button8).add(button11)
markup4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button8).add(button9)
markup5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button10)
markup6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button11)