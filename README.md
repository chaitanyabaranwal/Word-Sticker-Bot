# Word Sticker Bot ![Bot Logo](some.link.to.image "@WordStickerBot")

This Telegram bot stylizes any text sent by the user, and generates a sticker which is added to the user's individual sticker set.

How does it work? It converts the user's text message into an HTML string styled with various CSS elements according to the user's choice of fonts. The bot then converts the HTML string into a compressed PNG image via [imgkit](https://pypi.org/project/imgkit/) and [PIL](https://pypi.org/project/Pillow/2.2.1/). The user will automatically receive the sticker generated from our bot, added to their individual sticker set.

[Try it now!](something)

## Getting Started Locally

1. Create a Telegram bot and obtain an authentication token from [@BotFather](https://telegram.me/botfather) on Telegram.
2. Install requirements from [requirements.txt](link).
3. Replace your API token with the token in the `main()` function.
4. Run `python bot.py`.

## Deployment

The bot has been deployed on [Heroku](link), you can find it [here](link).

## Built With

* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) - The bot API used
* [imgkit](https://pypi.org/project/imgkit/) - for PNG image creation
* [PIL](https://pillow.readthedocs.io/en/stable/) - for PNG image compression

## Authors

* **Chaitanya Baranwal** - *CS Undergraduate, NUS* - [chaitanyabaranwal](https://github.com/chaitanyabaranwal)
* **Ong Yan Chun** - *CS Undergraduate, NUS* - [yaaanch](https://github.com/yaaanch)
* **Liu Zechu** - *CS Undergraduate, NUS* - [LiuZechu](https://github.com/LiuZechu)


## Acknowledgments
* Free time and lack of sleep
* This project was created during Hack&Roll 2019, a Hackathon organized by NUS Hackers.
