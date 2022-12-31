from aiogram import Dispatcher, executor, types, Bot
from tk import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)


@dp.message_handler()
async def count_symbols(msg: types.Message) -> None:
    await msg.answer(len(msg.text) - msg.text.count(' '))


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)
