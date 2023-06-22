

import os

from bot.utils.buttons import inlineButtons
from bot.utils.funcs import get_subdirs, index_to_path

from aiogram.utils.callback_data import CallbackData

path_cb = CallbackData('path', 'folder', 'level')


def get_message_data(path, level, n=2):
    level = int(level)
    spath = path.split('/')
    button_texts = get_subdirs(spath[:level+1], fromindex=1)
    button_texts.pop('files', [])

    button_info = sorted(button_texts.keys())
    markup = inlineButtons(button_info, '/'.join(spath[:level+1]), path_cb, level, n)

    dir_files = get_subdirs(spath, fromindex=1)
    dir_path = os.path.join('app', *index_to_path(spath))

    if level == 4 and len(dir_files) > 1:
        dir_path = os.path.join(dir_path, '01')

    text_path = img_path = dir_path
    text_path = os.path.join(text_path, 'text.txt')
    
    if level == 4:
        sub_files = get_subdirs(img_path.split('/')[1:]).pop('files', [])
        imgs = tuple(filter(lambda name: name.endswith(('.png', '.jpg', '.jpeg')), sub_files))
        img_path = os.path.join(img_path, imgs[0])
    
    text = 'The text file is missing!'
    if text_path:
        with open(text_path, 'r') as f:
            text = f.read()

    text = '\n\n'.join([
        dir_path[9:].replace('_', ' ').replace('/', ' -> '),
        text
    ])

    if level == 4:
        return text, img_path, markup
    return text, markup
