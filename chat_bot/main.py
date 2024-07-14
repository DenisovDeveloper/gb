import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from keyboards import kb1, kb2
from random_fox import fox

API_TOKEN = config.token
# Включаем логирование, чтобы видеть сообщения в консоли

logging.basicConfig(level=logging.INFO)
# Инициализация бота и диспетчера

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Хендлер на команду /start
# @dp.message(Command("start"))
# async def command_start(message: types.Message):
#     await message.answer("Привет! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")

# Хендлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)


# @dp.message(Command("ура"))
# async def send_ura(message: types.Message):
#     await message.answer("УРАААА! Я эхобот на aiogram 3. Отправь мне любое сообщение, и я повторю его.")

# Хендлер на команду /stop
@dp.message(Command("stop"))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')

    # Хендлер на команду /fox
@dp.message(Command('fox'))
@dp.message(Command('лиса'))
@dp.message(F.text.lower() == 'покажи лису')
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'держи лису, {name}')
    await message.answer_photo(photo=img_fox)



# Хендлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, - {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока, - {name}')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я - бот, - {name}')
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')



async def main():
    await dp.start_polling(bot)



# @dp.message()
# async def echo(message: types.Message):
#     if "ура" in message.text:
#         await message.answer("УРАААА!")
#     elif message.text == "инфо":
#         user_name = message.chat.id
#         print(user_name)
#         await message.answer(str(user_name))
#     else:
#         await message.answer(message.text)


# async def main():
#     await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
