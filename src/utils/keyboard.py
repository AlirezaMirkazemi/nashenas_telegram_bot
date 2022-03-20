
from telebot import types
import emoji


def create_keyboard(keys, row_width=2, resize_keyboard=True):
    """
    Creates a keyboard with the given keys.

    Example:
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    """
    markup = types.ReplyKeyboardMarkup(row_width=row_width, resize_keyboard=resize_keyboard)
    keys = map(emoji.emojize, keys)
    buttons = map(types.KeyboardButton, keys)
    markup.add(*buttons)

    return markup
