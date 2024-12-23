
from os import getenv
from dataclasses import dataclass


@dataclass
class Bot:
    token: str


@dataclass
class Webhook:
    host: str
    path: str

    app_host: str
    app_port: int

    @property
    def url(self):
        return self.host + self.path


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
            path=getenv('WEBHOOK_PATH'),
            app_host=getenv('APP_HOST'),
            app_port=int(getenv('APP_PORT'))
        )
    )
