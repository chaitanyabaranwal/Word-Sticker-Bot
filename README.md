# Word Sticker Bot ![Bot Logo](https://github.com/chaitanyabaranwal/WordArt_Telegram_Bot/blob/master/images/bot_logo.jpg =200x200)

This Telegram bot stylizes any text sent by the user, and generates a sticker which is added to the user's individual sticker set.

How does it work? It converts the user's text message into an HTML string styled with various CSS elements according to the user's choice of fonts. The bot then converts the HTML string into a compressed PNG image via [imgkit](https://pypi.org/project/imgkit/) and [PIL](https://pillow.readthedocs.io/en/stable/). The user will automatically receive the sticker generated from our bot, added to their individual sticker set.

[Try it now!](something)

## Features
1. `/text` prompts the user to enter text of at most 100 characters, and allows the user to select from around 30 fonts to create a sticker.
2. `/styles` displays all available styles, which are categorized into Basic, Bold, Fancy, Handwritten, Wordart, and Decorative.
3. `/default_style` sets the default style.
4. `/delete deletes` a previously created sticker. The user can send the sticker they want to delete or its index in the pack.
5. `/help` shows the help dialogue.

## Getting Started Locally
1. Create a Telegram bot and obtain an authentication token from [@BotFather](https://telegram.me/botfather) on Telegram.
2. Install requirements from `requirements.txt`.
3. Replace your API token with the token in the `main()` function.
4. Run `python bot.py`.

## Deployment
The bot has been deployed on [Heroku](https://www.heroku.com/), you can find it [here](link).

## Built With
* [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot) - The bot API used
* [imgkit](https://pypi.org/project/imgkit/) - for PNG image creation
* [PIL](https://pillow.readthedocs.io/en/stable/) - for PNG image compression

## Authors
**Team Ankrypt** ![Team Logo](https://github.com/chaitanyabaranwal/WordArt_Telegram_Bot/blob/master/images/ankrypt-logo.png =200x200)
* **Chaitanya Baranwal** - *CS Undergraduate, National University of Singapore (NUS)* - Github: [chaitanyabaranwal](https://github.com/chaitanyabaranwal)
* **Ong Yan Chun** - *National University of Singapore (NUS)* - Github: [yaaanch](https://github.com/yaaanch)
* **Liu Zechu** - *National University of Singapore (NUS)* - Github: [LiuZechu](https://github.com/LiuZechu)

## Acknowledgments
* Free time and lack of sleep
* This project was created during Hack&Roll 2019, a Hackathon organized by NUS Hackers.
