from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton('KB 1'), KeyboardButton('KB 2'), KeyboardButton('KB 3')],
        [KeyboardButton('KB 4'), KeyboardButton('KB 5'), KeyboardButton('KB 6')],
        [KeyboardButton('KB 7'), KeyboardButton('KB 8'), KeyboardButton('KB 9')],
    ])

    return kb
    