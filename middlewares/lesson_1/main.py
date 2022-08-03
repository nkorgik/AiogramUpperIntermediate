from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


class TestMiddleware(BaseMiddleware):

    async def on_process_update(self, update, data):
        print('sfjksdlfjlkas')

    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('Hello')


@dp.message_handler(commands=['start'])  # обработчик событий message
async def cmd_start(message: types.Message) -> None:
    await message.reply('Ты написал команду старт!')
    print('World!')


if __name__ == '__main__':
    dp.middleware.setup(TestMiddleware())
    executor.start_polling(dp,
                           skip_updates=True)
