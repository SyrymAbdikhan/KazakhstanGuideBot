
import logging

from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook

from bot.loader import bot, dp
from bot.config import Webhook


def register_all_middlewares(dispatcher: Dispatcher) -> None:
    logging.info('Registering middlewares')
    dispatcher.setup_middleware(LoggingMiddleware())


def register_all_filters(dispatcher: Dispatcher) -> None:
    logging.info('Registering filters')


def register_all_handlers(dispatcher: Dispatcher) -> None:
    from bot.handlers import common
    logging.info('Registering handlers')
    
    common.register_handlers(dispatcher)


async def register_all_commands(dispatcher: Dispatcher) -> None:
    logging.info('Registering commands')



async def on_startup(dispatcher: Dispatcher) -> None:
    register_all_middlewares(dispatcher)
    register_all_filters(dispatcher)
    register_all_handlers(dispatcher)
    await register_all_commands(dispatcher)
    
    bot = dispatcher.bot
    webhook_url = bot.config.webhook.url

    webhook = await bot.get_webhook_info()
    if webhook_url:
        await dispatcher.bot.set_webhook(webhook_url)
        logging.info('Webhook was set')
    elif webhook.url:
        await dispatcher.bot.delete_webhook()
        logging.info('Webhook was deleted')

    logging.info('Bot started!')


async def on_shutdown(dispatcher: Dispatcher) -> None:
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()
    logging.info('Bot shutdown!')


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    )
    logging.info('Initializing bot')

    webhook: Webhook = bot.config.webhook
    start_webhook(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        webhook_path=webhook.path,
        skip_updates=True,
        host=webhook.app_host,
        port=webhook.app_port
    )


if __name__ == '__main__':
    main()
