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

    # async def on_pre_process_update(self, update, data):
    #     print('update')

    async def on_process_callback_query(self, callback: types.CallbackQuery, data: dict):
        print('YES')


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('TEST', callback_data='data_test')]
    ])
    await message.reply('Ты нажал на команду старт',
                        reply_markup=ikb)


@dp.message_handler(lambda message: message.text.lower() == "привет")
async def text_hello(message: types.Message) -> None:
    print('handler')
    await message.reply('И тебе привет!')


@dp.callback_query_handler(text='data_test')
async def cb_test(callback: types.CallbackQuery):
    await callback.answer()


if __name__ == "__main__":
    dp.middleware.setup(AdminMiddleware())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)
