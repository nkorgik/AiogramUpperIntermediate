from aiogram import types, executor, Bot, Dispatcher
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


ADMIN = 5186850149


class CustomMiddleware(BaseMiddleware):

    async def on_process_message(self,
                                 message: types.Message,
                                 data: dict):

        if message.from_user.id != ADMIN:
            raise CancelHandler()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.reply('Ты нажал на команду старт')


@dp.message_handler(lambda message: message.text.lower() == "привет")
async def text_hello(message: types.Message) -> None:
    await message.reply('И тебе привет!')


if __name__ == "__main__":
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
