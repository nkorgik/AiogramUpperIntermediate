from aiogram import Dispatcher, executor, types, Bot # импорт основных элементов библиотеки
# Dispatcher - класс для создания диспетчера, отслеживающего обновления
# executor - объект по исполнению каких-либо задач
# types - модуль всех типов данных библиотеки
# Bot - класс для создания экземпляра (сущности) бота
from tk import TOKEN_API # импортирование токена


bot = Bot(token=TOKEN_API) # создание экземпляра бота
dp = Dispatcher(bot=bot) # создание экземпляра диспетчера


@dp.message_handler() # получение объекта декоратора
async def count_symbols(msg: types.Message) -> None: # объявление функции обработчика
    await msg.answer(len(msg.text) - msg.text.count(' ')) # ответ пользователю, где msg - объект сообщения, которое он нам отправил


if __name__ == "__main__": # классическая идиома языка питон для непосредственного запуска модуля
    executor.start_polling(dispatcher=dp) # запуск бота в режиме полинга
