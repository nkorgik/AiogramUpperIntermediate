"""Here is the information about request processing - Middlewares 2 part
In every single layer we can handle the certain type of data/events"""
# pre-process update
# process update
# pre-process message|callback_query
# filter (lambda message: not message.photo)
# process message|callback_query|...et cetera
# handler
# post process message
# post process update

from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


class CustomMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_update(self, update: types.Update, data: dict):
        pass

    async def on_process_message(self, message: types.Message, data: dict):
        print(data, message)


@dp.message_handler(commands=['start'])  # обработчик событий message
async def cmd_start(message: types.Message) -> None:
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Test', callback_data='data')],
    ])
    await message.reply('Ты написал команду старт!',
                        reply_markup=ikb)


if __name__ == '__main__':
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dp,
                           skip_updates=True)
