
from os import getenv
from dataclasses import dataclass


@dataclass
class Bot:
    token: str


@dataclass
class Webhook:
    host: str
    path: str
    url: str

    app_host: str
    app_port: int

    def __post_init__(self):
        self.url = self.host + self.path


@dataclass
class Config:
    bot: Bot
    webhook: Webhook


def load_config():
    return Config(
        bot=Bot(
            token=getenv('BOT_TOKEN')
        ),
        webhook=Webhook(
            host=getenv('WEBHOOK_HOST'),
            path=f"/bot/{getenv('BOT_TOKEN')}",
            url='',
            app_host=getenv('APP_HOST'),
            app_port=getenv('APP_PORT')
        )
    )
