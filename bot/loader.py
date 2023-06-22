
from aiogram import Bot, Dispatcher, types

from bot.config import Config, load_config

config: Config = load_config()
bot = Bot(config.bot.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
bot.config = config
