
import typing

from bot.utils.msg_constructor import get_message_data, path_cb

from aiogram import Dispatcher, types
from aiogram.utils import exceptions


async def cmd_menu(message: types.Message):
    text, markup = get_message_data(path='0', level=0)
    await message.answer(text, reply_markup=markup)


async def query_levels_0_to_3(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    text, markup = get_message_data(
        path=callback_data['folder'],
        level=callback_data['level']
    )
    if 'photo' in query.message:
        await query.message.delete()
        await query.message.answer(text, reply_markup=markup)
    else:
        await query.message.edit_text(text, reply_markup=markup)


async def query_level_4(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    text, img_path, markup = get_message_data(
        path=callback_data['folder'],
        level=callback_data['level'],
        n=5
    )
    
    if 'photo' in query.message:
        try:
            await query.message.edit_media(
                types.InputMediaPhoto(media=open(img_path, 'rb'), caption=text),
                reply_markup=markup
            )
        except exceptions.MessageNotModified:
            pass
    else:
        await query.message.delete()
        await query.message.answer_photo(
            photo=open(img_path, 'rb'),
            caption=text,
            reply_markup=markup
        )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_menu, commands="start")
    dp.register_message_handler(cmd_menu, commands="menu")
    dp.register_callback_query_handler(query_levels_0_to_3, path_cb.filter(level=['0', '1', '2', '3']))
    dp.register_callback_query_handler(query_level_4, path_cb.filter(level='4'))
