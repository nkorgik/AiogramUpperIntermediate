from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup([
        [KeyboardButton(row + column) for row in range(50)] for column in range(50)
    ])

    return kb
    