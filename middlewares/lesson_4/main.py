from aiogram import types, executor, Bot, Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler


from config import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


ADMIN = 5186850149


def set_key(key: str = None):

    def decorator(func):
        setattr(func, 'key', key)

        return func

    return decorator


class AdminMiddleware(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict):

        handler = current_handler.get()

        if handler:
            key = getattr(handler, 'key', 'Такого атрибута нет')
            print(key)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.reply('Ты нажал на команду старт')


@dp.message_handler(lambda message: message.text.lower() == "привет")
@set_key('hello!')
async def text_hello(message: types.Message) -> None:
    print('handler')
    await message.reply('И тебе привет!')


if __name__ == "__main__":
    dp.middleware.setup(AdminMiddleware())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
