#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from ImageGen import ImageGen
import telegram
import logging
import constants as c

CONVERT_TEXT, STYLE_SELECT, IMAGE_RESIZE, TEXT_TRANSFORM, DELETE_STICKER = range(5)
text = ''

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name) - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

#################################
# Standard bot commands #
#################################

def start(bot, update):
    update.message.reply_text(c.HELP_TEXT)

def help(bot, update):
    update.message.reply_text(c.HELP_TEXT)

def cancel(bot, update):
    text = 'Command cancelled!'
    update.message.reply_text(text)

def error(bot, update, error):
    logger.warning('Update caused error "%s"', error)

####################################
# Functions to handle text-styling #
####################################

def textConvert(bot, update):
    bot.send_message(update.message.chat_id, c.TEXT_CONVERT_TEXT, reply_to_message_id=update.message.message_id,
                        reply_markup=telegram.ForceReply())
    return STYLE_SELECT

def styles(bot, update):
    global text 
    text = update.message.text
    bot.send_message(update.message.chat_id, c.STYLE_TEXT, reply_to_message_id=update.message.message_id,
                        reply_markup=telegram.ForceReply())
    return CONVERT_TEXT

def transformText(bot, update):
    ImageGen(text, update.message.text)
    with open('test.png', 'rb') as f:
        file = bot.upload_sticker_file(update.message.from_user.id, f)
    assert file

    # Create/add to sticker pack and return sticker
    sticker_set_name = "WordArt_%s_by_HackandRoll_Testbot" % update.message.from_user['username']
    try:
        bot.add_sticker_to_set(update.message.from_user.id, sticker_set_name,
            file.file_id, '😄')
    except:
        bot.create_new_sticker_set(update.message.from_user.id, sticker_set_name, 
            "WordArt", file.file_id, '😄')
    finally:
        sticker_set = bot.get_sticker_set(sticker_set_name)
        bot.send_sticker(update.message.chat_id, sticker_set.stickers[-1])

    return ConversationHandler.END

########################################
# Functions to handle sticker deletion #
########################################

def delete(bot, update):
    update.message.reply_text(c.DELETE_STICKER)
    return DELETE_STICKER

def deleteSticker(bot, update):
    try:
        sticker_set_name = "WordArt_%s_by_HackandRoll_Testbot" % update.message.from_user['username']
        sticker_set = bot.get_sticker_set(sticker_set_name)
        bot.delete_sticker_from_set(sticker_set.stickers[int(update.message.text) - 1].file_id)
        update.message.reply_text("Sticker deleted!")
    except:
        update.message.reply_text("Sorry, sticker set does not exist. :(")

    return ConversationHandler.END

# Start the bot
def main():
    updater = Updater("***REMOVED***")
    dp = updater.dispatcher

    # Set up commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_error_handler(error)

    # Handler to manage text styling
    textConvertHandler = ConversationHandler(
        entry_points = [CommandHandler('text', textConvert)],
        states = {
            CONVERT_TEXT: [MessageHandler(Filters.text, transformText)],
            STYLE_SELECT: [MessageHandler(Filters.text, styles)],
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )
    dp.add_handler(textConvertHandler)

    # Handler to manage sticker deletion
    stickerDeleteHandler = ConversationHandler(
        entry_points = [CommandHandler('delete', delete)],
        states = {
            DELETE_STICKER: [MessageHandler(Filters.text, deleteSticker)]
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )
    dp.add_handler(stickerDeleteHandler)

    updater.start_polling()

    # Run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()