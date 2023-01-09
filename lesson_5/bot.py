import os
from PIL import ImageGrab
import secrets
from aiogram.dispatcher import filters
from aiogram import Dispatcher, executor, types, Bot # импорт основных элементов библиотеки
# Dispatcher - класс для создания диспетчера, отслеживающего обновления
# executor - объект по исполнению каких-либо задач
# types - модуль всех типов данных библиотеки
# Bot - класс для создания экземпляра (сущности) бота
from tk import TOKEN_API # импортирование токена
from kbs import get_kb

bot = Bot(token=TOKEN_API) # создание экземпляра бота
dp = Dispatcher(bot=bot) # создание экземпляра диспетчера


@dp.message_handler(filters.IsReplyFilter(is_reply='key'))
async def process_update(msg: types.Message) -> None:
    await msg.answer('Hello World!')


@dp.message_handler(commands=['start'])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('Text', reply_markup=get_kb())


@dp.message_handler(commands=['cancel'])
async def cmd_cancel(msg: types.Message) -> None:
    await msg.answer('Canceled', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['screen'])
async def cmd_screen(msg: types.Message) -> None:
    img = ImageGrab.grab()
    if not os.path.exists('static'):
        os.mkdir('static')
    os.chdir('static')
    img_name = secrets.token_hex(8) + '.png'
    img.save(img_name, format='PNG')

    await msg.answer_photo(photo=open(img_name, 'rb'))


# task_1
# @dp.message_handler(content_types="sticker")
# async def echo_sticker(msg: types.Message) -> None:
#     await msg.answer_sticker(sticker=msg.sticker.file_id)


# task_2
# @dp.message_handler(lambda msg: not msg.text.count(' '))
# async def handle_word(msg: types.Message) -> None:
#     await msg.answer("This sentence contains one word")

# @dp.message_handler(lambda msg: msg.text.count(' '))
# async def handle_rest(msg: types.Message) -> None:
#     await msg.answer("This sentence contains more than one word")

# @dp.message_handler(content_types='sticker')
# async def handle_sticker(msg: types.Message) -> None:
#     await msg.answer("This is sticker!")

# @dp.message_handler(content_types='photo')
# async def handle_photo(msg: types.Message) -> None:
#     await msg.answer("This is photo!")


# task 3
# @dp.message_handler(commands=['start'])
# async def cmd_start(msg: types.Message) -> None:
#     await msg.answer("Write the numbers!")


# @dp.message_handler(lambda msg: msg.text.replace(' ', '').isdigit())
# async def handle_numbers(msg: types.Message) -> None:
#     arr = msg.text.split(' ')
#     await msg.answer(sum([int(num) for num in arr])/len(arr))


@dp.message_handler(commands=["help", "start"])
async def cmd_start(msg: types.Message) -> None:
    await msg.answer('START || HELP')

@dp.message_handler(commands=["CMD", "MAN"])
async def cmd_man(msg: types.Message) -> None:
    await msg.answer('CMD || MAN')


# @dp.message_handler() # получение объекта декоратора
# async def count_symbols(msg: types.Message) -> None: # объявление функции обработчика
#     await msg.answer(len(msg.text) - msg.text.count(' ')) # ответ пользователю, где msg - объект сообщения, которое он нам отправил


if __name__ == "__main__": # классическая идиома языка питон для непосредственного запуска модуля
    executor.start_polling(dispatcher=dp, 
                            skip_updates=True) # запуск бота в режиме полинга
