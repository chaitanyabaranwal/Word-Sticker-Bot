#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from ImageGen import ImageGen
import telegram
import logging
import helpers as c

CONVERT_TEXT, STYLE_SELECT, IMAGE_RESIZE, TEXT_TRANSFORM, DELETE_STICKER, STYLE_CATEGORY_SELECT, SET_DEFAULT = range(7)
text = 'sample_text'
default_style = 'rainbow'

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
    return ConversationHandler.END

def styles(bot, update):
    update.message.reply_text("Here are the available styles!")
    bot.send_photo(update.message.chat_id, open('images/styles.png', 'rb'))

def error(bot, update, error):
    logger.warning('Update caused error "%s"', error)

####################################
# Functions to handle text-styling #
####################################

def textConvert(bot, update):
    bot.send_message(update.message.chat_id, c.TEXT_CONVERT_TEXT, reply_to_message_id=update.message.message_id,
                        reply_markup=telegram.ForceReply())
    return STYLE_CATEGORY_SELECT

def stylesCategory(bot, update):
    if len(update.message.text) > 100:
        update.message.reply_text("Text can't be over 100 characters!")
        return ConversationHandler.END
    global text 
    text = update.message.text
    custom_keyboard = c.style_categories
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(update.message.chat_id, c.STYLE_TEXT, reply_to_message_id=update.message.message_id,
                        reply_markup=reply_markup)
    return STYLE_SELECT

def stylesSelect(bot, update):
    if (update.message.text == 'Default'):
        transformText(bot, update)
        return ConversationHandler.END
    custom_keyboard = c.selectStyleCategory(update.message.text)
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    text = 'Select a style from the category!'
    bot.send_message(update.message.chat_id, text, reply_to_message_id=update.message.message_id,
                        reply_markup=reply_markup)
    return CONVERT_TEXT

def transformText(bot, update):
    if (update.message.text == 'Default'):
        ImageGen(text, default_style)
    else:
        ImageGen(text, update.message.text)
    with open('images/test.png', 'rb') as f:
        file = bot.upload_sticker_file(update.message.from_user.id, f)
    assert file

    # Create/add to sticker pack and return sticker
    username = update.message.from_user['username']
    sticker_set_name = "WordArt_%s_by_WordStickerBot" % username
    try:
        bot.add_sticker_to_set(update.message.from_user.id, sticker_set_name,
            file.file_id, '😄')
    except:
        bot.create_new_sticker_set(update.message.from_user.id, sticker_set_name, 
            "WordArt_by_%s" % username, file.file_id, '😄')
    finally:
        sticker_set = bot.get_sticker_set(sticker_set_name)
        if len(sticker_set.stickers) > 50:
            bot.delete_sticker_from_set(sticker_set.stickers[0])
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
        sticker_set_name = "WordArt_%s_by_WordStickerBot" % update.message.from_user['username']
        sticker_set = bot.get_sticker_set(sticker_set_name)
        bot.delete_sticker_from_set(sticker_set.stickers[int(update.message.text) - 1].file_id)
        update.message.reply_text("Sticker deleted!")
    except:
        update.message.reply_text("Sorry, sticker set does not exist. :(")

    return ConversationHandler.END

###############################################
# Functions to handle default style selection #
###############################################

def set_default(bot, update):
    custom_keyboard = c.style_categories_no_default
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(update.message.chat_id, c.STYLE_TEXT, reply_markup=reply_markup)
    return STYLE_SELECT

def stylesSelectDefault(bot, update):
    custom_keyboard = c.selectStyleCategory(update.message.text)
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    text = 'Select a style from the category!'
    bot.send_message(update.message.chat_id, text, reply_to_message_id=update.message.message_id,
                        reply_markup=reply_markup)
    return SET_DEFAULT

def changeDefault(bot, update):
    global default_style
    default_style = update.message.text
    update.message.reply_text('Okay! The default style is now ' + update.message.text + '.')
    return ConversationHandler.END

##################
# Start the bot #
##################
def main():
    updater = Updater("***REMOVED***")
    dp = updater.dispatcher

    # Set up commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("styles", styles))
    dp.add_error_handler(error)

    # Handler to manage text styling
    textConvertHandler = ConversationHandler(
        entry_points = [CommandHandler('text', textConvert)],
        states = {
            CONVERT_TEXT: [MessageHandler(Filters.text, transformText)],
            STYLE_SELECT: [MessageHandler(Filters.text, stylesSelect)],
            STYLE_CATEGORY_SELECT: [MessageHandler(Filters.text, stylesCategory)]
        },
        fallbacks = [CommandHandler('cancel', cancel)],
        conversation_timeout = 10.0,
    )
    dp.add_handler(textConvertHandler)

    # Handler to manage sticker deletion
    stickerDeleteHandler = ConversationHandler(
        entry_points = [CommandHandler('delete', delete)],
        states = {
            DELETE_STICKER: [MessageHandler(Filters.text, deleteSticker)]
        },
        fallbacks = [CommandHandler('cancel', cancel)],
        conversation_timeout = 10.0,
    )
    dp.add_handler(stickerDeleteHandler)

    # Handler to set default style
    defaultStyleHandler = ConversationHandler(
        entry_points = [CommandHandler('set_default', set_default)],
        states = {
            STYLE_SELECT: [MessageHandler(Filters.text, stylesSelectDefault)],
            SET_DEFAULT: [MessageHandler(Filters.text, changeDefault)]
        },
        fallbacks = [CommandHandler('cancel', cancel)],
        conversation_timeout = 10.0,
    )
    dp.add_handler(defaultStyleHandler)

    updater.start_polling()

    # Run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
