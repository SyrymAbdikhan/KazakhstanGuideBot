
import os

from aiogram import types


def inlineButtons(button_info, current_path, cb, level, n=2):
    markup = types.InlineKeyboardMarkup()

    nlevel = level
    if level < 4:
        nlevel += 1
    
    for i in range(0, len(button_info), n):
        row_info = button_info[i:i+n]
        buttons = []
        for text in row_info:
            path = os.path.join(current_path, str(button_info.index(text)))
            buttons.append(
                types.InlineKeyboardButton(
                    text.replace('_', ' '),
                    callback_data=cb.new( folder=path, level=nlevel)
                )
            )
        markup.row(*buttons)

    if level > 0:
        markup.add(
            types.InlineKeyboardButton(
                'Back',
                callback_data=cb.new(
                    folder=os.path.join(*current_path.split('/')[:-1]),
                    level=level-1
                )
            )
        )
    
    return markup
    
