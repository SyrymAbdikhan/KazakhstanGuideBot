# Kazakhstan Guide Bot

<div>
    <img src="https://i.imgur.com/rHD12Bw.png" width="300px">
    <img src="https://i.imgur.com/fAgQ4gJ.png" width="300px">
</div>

![python](https://img.shields.io/badge/python-v3.11.2-blue.svg?logo=python&logoColor=yellow) ![aiogram](https://img.shields.io/badge/aiogram-v2.25.1-blue.svg?logo=telegram) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

This interactive Telegram bot is specifically designed to provide comprehensive travel information to tourists visiting various cities in Kazakhstan. It helps visitors make the most of their stay by offering detailed, up-to-date information about local amenities and attractions. 

## Features

- Inline menu that repeats data structure
- Data is organized in hierarchical folders 

## Requirements

- Python v3.12.7
- Aiogram 2.25.1

## Installation

1. Clone this repository

    ```
    $ git clone https://github.com/SyrymAbdikhan/KazakhstanGuideBot.git
    $ cd KazakhstanGuideBot
    ```

2. Rename the file `.env.dist` to `.env` and replace the placeholders with required data.

- Create a new bot on Telegram by talking to the [BotFather](https://t.me/BotFather), and obtain the `BOT_TOKEN`.

3. Create a virtual environment and install required dependencies.

    ```
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```

4. Run the bot using `python -m bot`

- To run the bot with Docker `sudo docker compose up -d --build`
