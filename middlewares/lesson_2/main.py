"""Here is the information about request processing - Middlewares 2 part
In every single layer we can handle the certain type of data/events"""
# pre-process update
# process update
# pre-process message
# filter
# process message
# handler
# post process message
# post process update

from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)


def get_ikb() -> types.InlineKeyboardMarkup:
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Test', callback_data='blablabla')]
    ])

    return ikb


class TestMiddleware(BaseMiddleware):
    """custom Middleware class - let us process incoming request in different ways
    and on diverse layers"""
    async def on_pre_process_update(self,
                                    update: types.Update,
                                    data: dict):
        pass
        # print('This is pre process update!')
        # print(data, update, sep='\n')

    async def on_process_update(self,
                                update,
                                data):
        print('on process update')

    async def on_pre_process_message(self,
                                     message: types.Message,
                                     data: dict):
        print('on pre process message')


@dp.message_handler(commands=['start'])  # обработчик событий message
async def cmd_start(message: types.Message) -> None:
    await message.reply('Ты написал команду старт!',
                        reply_markup=get_ikb())


if __name__ == '__main__':
    dp.middleware.setup(TestMiddleware())
    executor.start_polling(dp,
                           skip_updates=True)
