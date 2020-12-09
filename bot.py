from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboard as kb
import slovar as sl
import random

bot = Bot(token='1438228814:AAHPjYCFXfuNjIf9xNXCr2HDAqGl4PSBlyE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start_cmd_handler(message: types.Message):
    await message.answer('Доброго времени суток! На сколько сегодня у вас был продуктивный день?', reply_markup=kb.markup1)

@dp.message_handler()
async def all_msg_handler(message: types.Message):
    button_text = message.text
    if button_text == "1 😞":
        await message.answer('Вы знаете в чем заключалась проблема?', reply_markup=kb.markup2)
    elif button_text == "2 😔":
        await message.answer('Вы знаете, что вышло из подконтроля?', reply_markup=kb.markup2)
    elif button_text == "3 😐":
        await message.answer('Что-то вышло из подконтроля?', reply_markup=kb.markup2)
    elif button_text == "4 🙂":
        await message.answer('Сможете завтра провести день на 5?', reply_markup=kb.markup2)
    elif button_text == "5 😁":
        await message.answer('Так держать! Уже есть планы на завтра?', reply_markup=kb.markup4)
        button_text = message.text

    if button_text == "Да":
        await message.answer('Обязательно займитесь этим завтра!', reply_markup=kb.markup3)
    elif button_text == "Нет":
        await message.answer('Не расстраиватейсь. У вас обязательно все получится', reply_markup=kb.markup3)

        button_text = message.text
    if button_text == "Совет от бота":
        x = sl.dict_sample[random.randint(1, 20)]
        await message.answer (x, reply_markup=kb.markup5)
    elif button_text == "Я знаю, что буду делать":
        await message.answer ('Не подведи себя!', reply_markup=kb.markup5)  

if __name__ == '__main__':
    executor.start_polling(dp)
